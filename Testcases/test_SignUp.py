import pytest
import openpyxl
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import logger
log = logger(__name__,logging.INFO)

class Test_SignUp(BaseTest):

    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password", dataProvider.get_data("LoginTest"))
    def test_doSignup(self, name, phoneNum, email, country, city, username, password):
        log.logger.info("Test Do Sign Up Started")
        regpage = RegistrationPage(self.driver)
        regpage.fillForm(name, phoneNum, email, country, city, username, password)
        log.logger.info("Test Do Sign Up Successfully executed")
