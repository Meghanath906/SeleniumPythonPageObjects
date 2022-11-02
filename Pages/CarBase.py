from selenium.webdriver.common.by import By

from Utilities import configReader
from Pages.BasePage import BasePage


class CarBase:
    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, configReader.readConfig("locators","cartitle_XPATH")).text

    def getCarNameAndPries(self):
        carNames = self.driver.find_elements(By.XPATH,configReader.readConfig("locators","carName_XPATH"))
        carPrices = self.driver.find_elements(By.XPATH,configReader.readConfig("locators","carPrice_XPATH"))

        for i in range(1,len(carPrices)):
            print((carNames[i].text+"---prices are ---"+carPrices[i].text).encode('utf8'))



