from datetime import datetime
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage


class TestE2Eone(BaseClass):


    def test_formsubmission(self, getData,setup):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        log.info("Opened the URL")
        homepage.entername().send_keys(getData["name"])
        log.info("Entered name: "+ getData["name"])
        homepage.entermail().send_keys(getData["mail"])
        log.info("Entered mail: "+ getData["mail"])
        homepage.enterpasswd().send_keys(getData["password"])
        log.info("Entered Password: "+ getData["password"])
        homepage.selchkbox().click()
        log.info("Selected the Checkbox")
        self.selOptionByTxt(homepage.selddoption(), getData["gender"])
        log.info("Selected the gender as "+ getData["gender"])
        homepage.selsubmitbtn().click()
        log.info("Submitted the form")
        homepage.getalertmsg("Success")
        self.driver.refresh()

    def test_e2e(self, setup):
        log = self.getLogger()
        self.driver.implicitly_wait(10)

        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems("Blackberry")
        log.info("Getting the Card Titles")
        checkoutpage.getappcard().click()
        log.info("Selected the required Mobile")
        checkoutpage.getshpcheckoutbtn().click()
        log.info("Moving to Card Checkout page")
        purchasepage = checkoutpage.getfnlcheckoutbtn()
        purchasepage.entercountry().send_keys("ind")
        self.verifyLinkPresence("India")
        purchasepage.selectcountry().click()
        log.info("Selected the country")
        purchasepage.selectchkbox().click()
        purchasepage.selectsubmit().click()
        log.info("Submitted the Purchasing successfully")
        purchasepage.chksuccess("Success")

    @pytest.fixture(params=HomePageData.getTestData("Test2"))
    def getData(self, request):
        return request.param