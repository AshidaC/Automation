from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    #  products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    #  product.find_element_by_xpath("div/button").click()
    #  product.find_element_by_xpath("div/h4/a").text
    #  find_element_by_css_selector("a[class*='btn-primary']").click()

    CardTitle = (By.CSS_SELECTOR, ".card-title a")
    CardFooter = (By.CSS_SELECTOR, ".card-footer button")
    ProductName = (By.XPATH, "/div/h4/a")
    CheckOut = (By.XPATH, "//a[contains(text(),'Checkout')]")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.CardTitle)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.ProductName)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.CardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.CheckOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
