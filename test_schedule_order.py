from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType
import unittest
import json
import names
import time
import random
from datetime import date
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from locators import checkoutlocators, productlocators, ordertypeselectors
from methods import future_date, later_order_setting, today_order_setting, select_combo_item
from methods import fetching_website, execute_click_by_product, select_product, sign_in
from methods import add_to_bag_and_verify_cart_details, Checkout_to_paymentscreen, place_ur_order_from_payment


class TestBestInTownpizzabase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:/Users/Digital Suppliers/Documents/GitHub/bestintown/chromedriver.exe")
        f = open('data.json', "r")
        data = json.loads(f.read())
        fetching_website(self.driver, data["url"])
        f.close()

    def tearDown(self):
        self.driver.quit()


class TestOrderSettings(TestBestInTownpizzabase):

    @allure.description("To verify that we can schedule our order for later days as well")
    def test_01_later_order_type(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            later_order_setting(self.driver, "12:45 PM")
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["combo_item"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details_combo(self.driver)
                Checkout_to_paymentscreen(self.driver)
                time.sleep(3)
                place_ur_order_from_payment(self.driver, "Delivery")
                time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify that we are able to place an order for today at any other time.")
    def test_02_todays_order(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            today_order_setting(self.driver, "01:45 PM")
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["combo_item"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details_combo(self.driver)
                Checkout_to_paymentscreen(self.driver)
                time.sleep(3)
                place_ur_order_from_payment(self.driver, "Delivery")
                time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e


if __name__ == '__main__':

    unittest.main()
