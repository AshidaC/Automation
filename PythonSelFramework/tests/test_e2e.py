import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        time.sleep(3)
        checkOutPage = homePage.shopItems()
        time.sleep(3)
        log.info("Getting all the titles")
        # checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitles()

        # //div[@class='card h-100']/div/h4/a
        # product = //div[@class='card h-100
        time.sleep(3)
        i = -1
        for product in products:
            i = i + 1
            log.info('a:' + product.text)
            if product.text == "Blackberry":
                # Add item to the cart
                time.sleep(3)
                checkOutPage.getCardFooter()[i].click()
        time.sleep(3)
        confirmPage = checkOutPage.checkOutItems()
        time.sleep(3)
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmPage.getCheckOutLast()
        # self.driver.find_element_by_id("country").send_keys("ind")
        time.sleep(3)
        log.info("entering country name as ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type =submit]").click()
        SuccessMessage = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text recievd from application is"+SuccessMessage)
        assert "Success! Thank you!" in SuccessMessage
        self.driver.get_screenshot_as_file("screen.png")
