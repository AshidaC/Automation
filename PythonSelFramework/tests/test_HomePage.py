import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        print(getData)
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("get firstname is "+getData["Firstname"])
        homepage.getName().send_keys(getData["Firstname"])
        homepage.getMail().send_keys(getData["Mail"])
        homepage.getPassword().send_keys(getData["Password"])
        time.sleep(2)
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        time.sleep(2)
        homepage.getExample().click()
        homepage.getSubmit().click()
        message = homepage.getSuccess().text
        assert "success" in message
        self.driver.refresh()

    # @pytest.fixture(params=[("ashida", "ashida.ch@gmail.com", "ashida@123", "Female"), ("aslam", "aslam@gmail.com", "aslam@123" ,"Male")])
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
