from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

import pytest

class TestHomePage1(BaseClass):

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

    @pytest.fixture(params=[{"name": "Sunderrajan Srinivasan", "mail": "ssrrajan@gmail.com", "password": "ssrrajan123", "gender": "Male"},{"name": "Pavithra Sunderrajan","mail": "pavit88@gmail.com","password": "pavithra123","gender": "Female"}])
    def getData(self, request):
        return request.param