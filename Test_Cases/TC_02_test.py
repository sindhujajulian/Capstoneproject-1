import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase2:

    def test_tc_login_02(self):

        _expected_error_msg = "Invalid credentials"
        actual_error_msg = HrmFunctionalities().invalid_login()
        assert actual_error_msg == _expected_error_msg
        print(actual_error_msg)  # Printing the error message
