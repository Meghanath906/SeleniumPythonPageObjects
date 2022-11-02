import time

import pytest
import openpyxl

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Pages.NewCarPage import NewCarsPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import logger

log = logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("*******Inside New Car Test*******")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle",
                             dataProvider.get_data("NewCarTest"))
    def test_SelectCars(self, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("car Brand is: ", carBrand)
        if carBrand == ["BMW"]:
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

        elif carBrand == ["Hyundai"]:
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

        elif carBrand == ["Toyota"]:
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

        elif carBrand == ["Honda"]:
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

    @pytest.mark.parametrize("carBrand,carTitle",
                             dataProvider.get_data("NewCarTest"))
    def test_printCarNamesandPrices(self, carBrand, carTitle):
        log.logger.info("******Inside print Cars Names and Prices Test*******")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("car Brand is: ", carBrand)
        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPries()

        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPries()

        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPries()

        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPries()
