"""Unit tests for synology_api.auth."""

import unittest

from synology_api.auth import Authentication
from synology_api.error_codes import CODE_SUCCESS, CODE_UNKNOWN


class GetErrorCodeTests(unittest.TestCase):
    """Tests for Authentication._get_error_code (a @staticmethod)."""

    def _call(self, response):
        return Authentication._get_error_code(response)

    # --- success ---

    def test_success_true_returns_zero(self):
        self.assertEqual(self._call({'success': True}), CODE_SUCCESS)

    def test_success_true_with_extra_data(self):
        self.assertEqual(self._call({'success': True, 'data': {'sid': 'x'}}), CODE_SUCCESS)

    # --- normal error ---

    def test_normal_error_returns_code(self):
        self.assertEqual(self._call({'success': False, 'error': {'code': 100}}), 100)

    def test_normal_error_returns_code_with_extras(self):
        response = {'success': False, 'error': {'code': 401, 'errors': []}}
        self.assertEqual(self._call(response), 401)

    # --- malformed responses (regression for AttributeError on
    #     `response.get('error').get('code')` when 'error' is missing/None) ---

    def test_missing_error_key_returns_unknown(self):
        # Was: AttributeError because response.get('error') → None, then None.get('code').
        self.assertEqual(self._call({'success': False}), CODE_UNKNOWN)

    def test_error_is_none_returns_unknown(self):
        self.assertEqual(self._call({'success': False, 'error': None}), CODE_UNKNOWN)

    def test_error_is_empty_dict_returns_unknown(self):
        self.assertEqual(self._call({'success': False, 'error': {}}), CODE_UNKNOWN)

    def test_error_is_non_dict_returns_unknown(self):
        # Server returning a string/list where a dict is expected.
        self.assertEqual(self._call({'success': False, 'error': 'oops'}), CODE_UNKNOWN)
        self.assertEqual(self._call({'success': False, 'error': [1, 2, 3]}), CODE_UNKNOWN)

    def test_error_code_is_non_int_returns_unknown(self):
        self.assertEqual(self._call({'success': False, 'error': {'code': 'NaN'}}), CODE_UNKNOWN)

    def test_completely_empty_response_returns_unknown(self):
        self.assertEqual(self._call({}), CODE_UNKNOWN)


class GetErrorDetailsTests(unittest.TestCase):
    """Tests for Authentication._get_error_details (a @staticmethod)."""

    def _call(self, response):
        return Authentication._get_error_details(response)

    # --- valid error details ---

    def test_file_station_shape(self):
        # Per https://kb.synology.com/en-global/DG/DSM_Login_Web_API_Guide/2
        response = {
            'success': False,
            'error': {
                'code': 1100,
                'errors': [{'code': 408, 'path': '/test/:'}],
            },
        }
        self.assertEqual(self._call(response), [{'code': 408, 'path': '/test/:'}])

    def test_active_directory_shape(self):
        # Per docstrings in directory_server.py.
        response = {
            'success': False,
            'error': {
                'code': 10104,
                'errors': [{'code': 10237, 'msg': 'ldb updaterecords: modify'}],
            },
        }
        self.assertEqual(
            self._call(response),
            [{'code': 10237, 'msg': 'ldb updaterecords: modify'}],
        )

    def test_multiple_details_preserved_in_order(self):
        response = {
            'success': False,
            'error': {
                'code': 1100,
                'errors': [
                    {'code': 408, 'path': '/a'},
                    {'code': 414, 'path': '/b'},
                ],
            },
        }
        self.assertEqual(
            self._call(response),
            [{'code': 408, 'path': '/a'}, {'code': 414, 'path': '/b'}],
        )

    # --- absent / empty ---

    def test_success_response_returns_empty(self):
        self.assertEqual(self._call({'success': True, 'data': {}}), [])

    def test_error_without_errors_key_returns_empty(self):
        self.assertEqual(self._call({'success': False, 'error': {'code': 100}}), [])

    def test_empty_errors_list_returns_empty(self):
        response = {'success': False, 'error': {'code': 1100, 'errors': []}}
        self.assertEqual(self._call(response), [])

    # --- malformed responses (mirror the defensive style of _get_error_code) ---

    def test_missing_error_key_returns_empty(self):
        self.assertEqual(self._call({'success': False}), [])

    def test_error_is_none_returns_empty(self):
        self.assertEqual(self._call({'success': False, 'error': None}), [])

    def test_error_is_non_dict_returns_empty(self):
        self.assertEqual(self._call({'success': False, 'error': 'oops'}), [])
        self.assertEqual(self._call({'success': False, 'error': [1, 2, 3]}), [])

    def test_errors_is_non_list_returns_empty(self):
        # Server returning a dict/string where a list is expected.
        self.assertEqual(self._call({'success': False, 'error': {'code': 1, 'errors': {'code': 2}}}), [])
        self.assertEqual(self._call({'success': False, 'error': {'code': 1, 'errors': 'oops'}}), [])

    def test_non_dict_entries_are_filtered_out(self):
        response = {
            'success': False,
            'error': {
                'code': 1100,
                'errors': [
                    {'code': 408, 'path': '/a'},
                    'garbage',
                    None,
                    42,
                    {'code': 414, 'path': '/b'},
                ],
            },
        }
        self.assertEqual(
            self._call(response),
            [{'code': 408, 'path': '/a'}, {'code': 414, 'path': '/b'}],
        )

    def test_completely_empty_response_returns_empty(self):
        self.assertEqual(self._call({}), [])


if __name__ == '__main__':
    unittest.main()
