from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

import pytest

class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.entername().send_keys(getData[0])
        homepage.entermail().send_keys(getData[1])
        homepage.enterpasswd().send_keys(getData[2])
        homepage.selchkbox().click()
        self.selOptionByTxt(homepage.selddoption(), getData[3])
        homepage.selsubmitbtn().click()
        homepage.getalertmsg("Success")
        self.driver.refresh()

    @pytest.fixture(params=[("Sunderrajan Srinivasan","ssrrajan@gmail.com","ssrrajan123","Male"),("Pavithra Sunderrajan","pavit88@gmail.com","pavithra123","Female")])
    def getData(self, request):
        return request.param