import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase4:

    def test_tc_pim_02(self):

        _expected_successful_msg = "Successfully Updated"
        success_text = HrmFunctionalities().edit_user_pim()
        assert success_text == _expected_successful_msg
        print(success_text)  # Printing the Successfully Updated message
