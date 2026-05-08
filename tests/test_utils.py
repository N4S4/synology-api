"""Unit tests for synology_api.utils."""

import unittest

from synology_api.utils import validate_path


class ValidatePathTests(unittest.TestCase):
    """Tests for validate_path covering both str and list inputs."""

    # --- str input: positive cases ---

    def test_str_valid_file(self):
        self.assertTrue(validate_path('/Downloads/script.log'))

    def test_str_valid_file_with_internal_space(self):
        self.assertTrue(validate_path('/Downloads/script log.txt'))

    def test_str_valid_extensionless(self):
        self.assertTrue(validate_path('/Downloads/script'))

    # --- str input: negative cases ---

    def test_str_trailing_slash(self):
        self.assertFalse(validate_path('/Downloads/folder/'))

    def test_str_trailing_space(self):
        self.assertFalse(validate_path('/Downloads/script.log '))

    def test_str_trailing_tab(self):
        self.assertFalse(validate_path('/Downloads/script.log\t'))

    def test_str_missing_leading_slash(self):
        self.assertFalse(validate_path('Downloads/script.log'))

    def test_str_space_after_extension(self):
        self.assertFalse(validate_path('/Downloads/script.log extra'))

    # --- list input: positive cases ---

    def test_list_all_valid(self):
        self.assertTrue(validate_path(['/Downloads/a.log', '/Downloads/b.log']))

    # --- list input: negative cases (these caught the closure bug) ---

    def test_list_single_with_trailing_slash(self):
        # Regression: prior to the fix, the trailing-slash check used the outer
        # `path` (the whole list) instead of `single_path`, so this returned True.
        self.assertFalse(validate_path(['/Downloads/folder/']))

    def test_list_single_with_trailing_space(self):
        # Regression: same closure bug — trailing-space check was skipped.
        self.assertFalse(validate_path(['/Downloads/script.log ']))

    def test_list_first_element_invalid(self):
        # Regression: the trailing-char check looked at path[-1] (last list
        # element), so an invalid first element could still pass the check.
        self.assertFalse(validate_path(['/Downloads/folder/', '/Downloads/ok.log']))

    def test_list_middle_element_invalid(self):
        self.assertFalse(validate_path(['/a.log', '/bad/folder/', '/b.log']))

    # --- input-type handling ---

    def test_non_str_non_list_returns_false(self):
        self.assertFalse(validate_path(123))
        self.assertFalse(validate_path(None))

    def test_list_with_non_str_element_returns_false(self):
        self.assertFalse(validate_path(['/a.log', 42]))


if __name__ == '__main__':
    unittest.main()
