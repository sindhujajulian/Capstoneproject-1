import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase3:

    def test_tc_pim_01(self):

        _expected_successful_msg = "Successfully Saved"
        success_text = HrmFunctionalities().creating_user_in_pim_module()
        assert success_text == _expected_successful_msg
        print(success_text)  # printing the successfully saved msg
