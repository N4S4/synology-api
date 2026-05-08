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


if __name__ == '__main__':
    unittest.main()
