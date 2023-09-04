from Test_Data import user_credentials
from Test_Locators.locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.select import Select


class HrmFunctionalities:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.my_wait = WebDriverWait(self.driver, 10)
        self.locators = LoginPageLocators
        self.url = user_credentials.url
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def login_to_hrm(self):
        """
        Logging into HRM with valid credentials
        :return: None
        """
        username_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.username_ele_xpath)))
        username_ele.send_keys(user_credentials.user_name)
        password_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.NAME, self.locators.password_ele_name_tag)))
        password_ele.send_keys(user_credentials.right_password_for_login)
        login_btn_ele = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.login_btn_xpath)))
        login_btn_ele.click()
        # return self.driver.title

    def page_title(self):
        """
        Getting the title of successful
        :return: title
        """
        self.login_to_hrm()
        return self.driver.title

    def invalid_login(self):
        """
        Logging into HRM with invalid credentials
        :return: error msg of invalid credentials
        """
        username_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.username_ele_xpath)))
        username_ele.send_keys(user_credentials.user_name)

        password_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.NAME, self.locators.password_ele_name_tag)))  # locating the password

        password_ele.send_keys(user_credentials.wrong_password_for_login)
        login_btn_ele = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.login_btn_xpath)))

        login_btn_ele.click()

        error_ele = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.alert_xpath)))

        return error_ele.text  # getting error text of invalid credentials

    def creating_user_in_pim_module(self):
        """
        creating a user in PIM Module.
        :return: successful msg of user creation.
        """
        self.login_to_hrm()

        pim_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.pim_xpath)))
        pim_element.click()

        add_button = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.add_user_xpath)))
        add_button.click()

        first_name_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.first_name_xpath)))
        first_name_element.send_keys(user_credentials.first_name)

        middle_name_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.middle_name_xpath)))
        middle_name_ele.send_keys(user_credentials.middle_name)

        last_name_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.last_name_xpath)))
        last_name_element.send_keys(user_credentials.last_name)

        employee_id_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.employee_id_xpath)))
        #employee_id_element.click()
        employee_id_element.clear()
        employee_id_element.send_keys(user_credentials.employee_id)


        create_login_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.create_login_details_xpath)))
        create_login_element.click()

        username_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.username_pim_xpath)))
        username_element.send_keys(user_credentials.username_pim)

        password_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.password_xpath)))
        password_element.send_keys(user_credentials.password)

        confirm_password_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.confirm_password_xpath)))

        confirm_password_element.send_keys(user_credentials.confirm_password)
        button_ele = self.driver.find_element(By.XPATH, self.locators.btn_xpath)
        button_ele.click()

        nickname_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.nickname_xpath)))
        nickname_element.send_keys(user_credentials.nick_name)

        driving_license_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.driving_license_xpath)))
        driving_license_element.send_keys(user_credentials.driving_license_no)

        license_expiry_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.license_expiry_xpath)))


        license_expiry_element.send_keys(user_credentials.license_expiry_date)


        dob_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.dob_xpath)))
        dob_element.send_keys(user_credentials.date_of_birth)


        select_option_elements = self.my_wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.select_ele_xpath)))

        select_option_elements[0].click()

        indian_element = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.indian_ele_xpath)))
        indian_element.click()

        select_option_elements[1].click()

        marital_status_element = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.single_ele_xpath)))
        marital_status_element.click()

        military_service_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.military_service_xpath)))
        military_service_element.send_keys(user_credentials.military_service)


        save_btns = self.my_wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.locators.save_btn_xpath)))

        save_btns[0].click()

        select_option_elements[2].click()
        blood_group = self.my_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.locators.blood_grp_ele_xpath)))
        blood_group.click()

        save_btns[1].click()
        success_message_element = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.successful_msg_xpath)))

        return success_message_element.text

    def edit_user_pim(self):
        """
        Editing details  of a existing user
        :return:  Successfully modified message
        """

        self.login_to_hrm()
        pim_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.pim_xpath)))
        pim_element.click()

        employee_list_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.employee_list_xpath)))
        employee_list_ele.click()

        all_emp_ids = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_ids_xpath)))
        count_of_all_users = len(all_emp_ids)

        all_emp_last_names = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_last_names)))

        all_emp_edit_btns = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_edit_btns)))

        for i in range(0, count_of_all_users):
            employee_id = all_emp_ids[i].text
            employee_last_name = all_emp_last_names[i].text
            emp_no = employee_id[4:]
            edit_ele = all_emp_edit_btns[i]
            #
            if emp_no == user_credentials.employee_id and employee_last_name == user_credentials.last_name:

                edit_ele.click()
                nickname_ele1 = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.nickname_xpath)))
                nickname_ele1.clear()
                nickname_ele1.send_keys(user_credentials.updated_nick_name)  # sending a nick_name value

                military_service_ele1 = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.military_service_xpath)))
                military_service_ele1.click()
                military_service_ele1.clear()

                military_service_ele1.send_keys(user_credentials.military_service)  # sending a military ele value

                save_btn1 = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.save_btn_for_updated_details)))

                save_btn1.click()

                success_msg = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.updated_success_msg)))

                success_text = success_msg.text
                return success_text

    def delete_id_user(self):

        """
        Delete a user from employee list
        :return: Successfully deletion message
        """
        self.login_to_hrm()

        pim_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.pim_xpath)))
        pim_element.click()

        employee_list_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.employee_list_xpath)))
        employee_list_ele.click()

        all_emp_ids = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_ids_xpath)))
        count_of_all_users = len(all_emp_ids)

        all_emp_last_names = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_last_names)))

        all_emp_delete_btns = self.my_wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.all_emp_delete_btns)))

        for i in range(0, count_of_all_users):

            employee_id = all_emp_ids[i]

            no = employee_id.text
            emp_no1 = no[4:]

            last_name_ele = all_emp_last_names[i]
            last_name1 = last_name_ele.text

            delete_ele = all_emp_delete_btns[i]

            if emp_no1 == user_credentials.employee_id and last_name1 == user_credentials.last_name:
                delete_ele.click()

                delete_yes_btn = self.my_wait.until(
                    EC.element_to_be_clickable((By.XPATH, self.locators.delete_btn_xpath)))

                delete_yes_btn.click()

                delete_msg_ele = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.deleted_msg_xpath)))

                delete_text = delete_msg_ele.text
                return delete_text


obj = HrmFunctionalities()
# obj.login_to_hrm()
# obj.page_title()
# obj.invalid_login()
obj.creating_user_in_pim_module()
# obj.edit_user_pim()
# obj.delete_id_user()
