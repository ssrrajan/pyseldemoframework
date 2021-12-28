from selenium.webdriver.common.by import By
from datetime import datetime


class PurchasePage:

    countrytxt = (By.ID, "country")
    selcountry = (By.LINK_TEXT, "India")
    chkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchasebtn = (By.XPATH, "//input[@type='submit']")
    scscaption = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")



    def __init__(self, driver):
        self.driver = driver

    def entercountry(self):
        return self.driver.find_element(*PurchasePage.countrytxt)

    def selectcountry(self):

        return self.driver.find_element(*PurchasePage.selcountry)

    def selectchkbox(self):
        return self.driver.find_element(*PurchasePage.chkbox)

    def selectsubmit(self):
        return self.driver.find_element(*PurchasePage.purchasebtn)

    def chksuccess(self,SuccessTxt):

        assert SuccessTxt in self.driver.find_element(*PurchasePage.scscaption).text

        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")
        self.driver.get_screenshot_as_file("C:\\Users\\pg0046\\PycharmProjects\\pyseldemoframework\\Evidenses\\purchasepagescrsht" + "_" + time + ".png")