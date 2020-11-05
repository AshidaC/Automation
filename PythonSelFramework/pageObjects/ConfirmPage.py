from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        # self.driver.find_element_by_id("country").send_keys("ind")

    CheckOutFinal = (By.XPATH, "//button[@class='btn btn-success']")
    Country = (By.ID, "country")

    def getCheckOutLast(self):
        self.driver.find_element(*ConfirmPage.CheckOutFinal).click()
        self.driver.find_element(*ConfirmPage.Country).send_keys("ind")





