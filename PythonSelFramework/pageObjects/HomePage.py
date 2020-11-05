from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@type='password']" )
    gender = (By.ID, "exampleFormControlSelect1")
    example = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    # driver.find_element_by_css_selector("a[href*='shop']").click()
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    # driver.find_element_by_name("name").send_keys("Ashida")
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    # driver.find_element_by_css_selector("input[name='email']").send_keys("ashida.chy@gmail.com")
    def getMail(self):
        return self.driver.find_element(*HomePage.email)

    # driver.find_element_by_id("exampleInputPassword1").send_keys("ashida@123")
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    # driver.find_element_by_id("exampleFormControlSelect1")
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    # driver.find_element_by_id("exampleCheck1").click()
    def getExample(self):
        return self.driver.find_element(*HomePage.example)

    # driver.find_element_by_xpath("//input[@type='submit']").click()
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    # driver.find_element_by_class_name("alert-success")
    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)









