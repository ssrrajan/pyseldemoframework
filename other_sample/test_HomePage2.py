from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

import pytest

class TestHomePage2(BaseClass):

    def test_formsubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.entername().send_keys(getData["name"])
        homepage.entermail().send_keys(getData["mail"])
        homepage.enterpasswd().send_keys(getData["password"])
        homepage.selchkbox().click()
        self.selOptionByTxt(homepage.selddoption(), getData["gender"])
        homepage.selsubmitbtn().click()
        homepage.getalertmsg("Success")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param