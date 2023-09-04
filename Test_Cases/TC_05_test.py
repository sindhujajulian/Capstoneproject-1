import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase5:

    def test_tc_pim_03(self):

        _expected_msg = "Successfully Deleted"
        deleted_text = HrmFunctionalities().delete_id_user()
        assert deleted_text == _expected_msg
        print(deleted_text)  # print Successfully Deleted Msg
