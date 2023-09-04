import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCases1:

    def test_tc_login_01(self):

        _expected_title = "OrangeHRM"
        actual_title = HrmFunctionalities().page_title()
        assert actual_title == _expected_title
        print("The user is logged in successfully")  # returning the successful message
