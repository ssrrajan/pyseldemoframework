from selenium.webdriver.common.by import By

from PageObjects.PurchasePage import PurchasePage


class CheckoutPage:

    shpcheckoutbtn = (By.XPATH, "//div[@id='navbarResponsive']/ul/li/a")
    appcardlist = (By.XPATH, "//div[@class='row']/div[2]/app-card-list/app-card")
    fnlcheckoutbtn = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver,cardText):
        self.driver = driver
        self.cardText = cardText

    def getappcard(self):
        for i in range(1, len(self.driver.find_elements(*CheckoutPage.appcardlist)) + 1):
            if self.driver.find_element(By.XPATH, value="{}{}{}".format("//div[@class='row']/div[2]/app-card-list/app-card[", i, "]/div/div[1]/h4/a")).text == self.cardText:
                appcard = (By.XPATH,"{}{}{}".format("//div[@class='row']/div[2]/app-card-list/app-card[", i,"]/div/div[2]/button"))
                return self.driver.find_element(*appcard)
                break

    def getshpcheckoutbtn(self):
        return self.driver.find_element(*CheckoutPage.shpcheckoutbtn)

    def getfnlcheckoutbtn(self):
        self.driver.find_element(*CheckoutPage.fnlcheckoutbtn).click()
        purchasepage = PurchasePage(self.driver)
        return purchasepage