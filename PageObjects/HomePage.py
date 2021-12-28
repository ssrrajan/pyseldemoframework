from datetime import datetime

from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckoutPage

class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    passwd = (By.ID, "exampleInputPassword1")
    chkbox = (By.ID, "exampleCheck1")
    ddoption = (By.ID, "exampleFormControlSelect1")
    submitbtn = (By.CLASS_NAME, "btn-success")
    alertmsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def __init__(self, driver):
        self.driver = driver

    def shopItems(self,cardText):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver, cardText)
        return checkoutpage

    def entername(self):
        return self.driver.find_element(*HomePage.name)

    def entermail(self):
        return self.driver.find_element(*HomePage.email)

    def enterpasswd(self):
        return self.driver.find_element(*HomePage.passwd)

    def selchkbox(self):
        return self.driver.find_element(*HomePage.chkbox)

    def selddoption(self):
        return self.driver.find_element(*HomePage.ddoption)

    def selsubmitbtn(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def getalertmsg(self, SuccessTxt):
        assert SuccessTxt in self.driver.find_element(*HomePage.alertmsg).text

        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")
        self.driver.get_screenshot_as_file("C:\\Users\\pg0046\\PycharmProjects\\pyseldemoframework\\Evidenses\\homepagescrsht" + "_" + time + ".png")