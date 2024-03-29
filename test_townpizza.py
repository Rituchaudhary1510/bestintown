from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType
import unittest
import json
import names
import time
import random
from random import randint
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from locators import checkoutlocators, productlocators
from methods import fetching_website, execute_click_by_product, select_product, sign_in, select_pizza_sides
from methods import add_to_bag_and_verify_cart_details, Checkout_to_paymentscreen, place_ur_order_from_payment
from methods import edit_items, delete_items_empty_cart, increase_item_in_cart, decrease_item_in_cart
from methods import order_setting, order_history, select_combo_item, verify_order_details


class TestBestInTownpizzabase(unittest.TestCase):

    def setUp(self):

        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/Desktop/BEST_IN_TOWN/chromedriver.exe", options=chrome_options)

        self.driver = webdriver.Chrome(
            "C:/Users/Digital Suppliers/Documents/GitHub/bestintown/chromedriver.exe")
        f = open('data.json', "r")
        data = json.loads(f.read())
        fetching_website(self.driver, data["url"])
        f.close()

    def tearDown(self):
        self.driver.quit()


class TestTownpizza(TestBestInTownpizzabase):

    @allure.description("To change order setting to pickup")
    def test_01_Pickup_order_setting(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(3)
            sign_in(self.driver, data["username3"], data["password"])
            order_setting(self.driver, "Pickup")
            time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify that one is able to add item to bag")
    def test_02_Add_product_to_bag(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
                # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify cart details")
    def test_03_Add_product_to_bag_verify_cart_details(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
                # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify add product and checkout to payment screen")
    def test_04_add_product_and_checkout_to_paymentscreen(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
                Checkout_to_paymentscreen(self.driver)
                time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify place order from payment screen")
    def test_05_place_final_order_from_paymentscreen(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
                Checkout_to_paymentscreen(self.driver)
                time.sleep(3)
                place_ur_order_from_payment(self.driver, "Delivery")
                time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify items can be edited")
    def test_06_edit_added_items(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["menulist_pizza3"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "medium",
                                   "thin", m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
                edit_items(self.driver)
                add_to_bag_and_verify_cart_details(self.driver)

            Checkout_to_paymentscreen(self.driver)
            place_ur_order_from_payment(self.driver, "Delivery")
            time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify cart is empty after items are deleted from the cart")
    def test_07_delete_items_from_cart(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["menulist_pizza3"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "medium",
                                   "thin", m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            delete_items_empty_cart(self.driver)
            print("Test case 07 ran successfully")
            # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify additional toppings of the item")
    def test_08_verify_add_additional_toppings(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["menulist_pizza3"]:
                print(m)
                execute_click_by_product(self.driver, m)
                time.sleep(5)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(
                    self.driver, "medium", "thin", m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
                time.sleep(2)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            print("Test case 08 ran successfully")
            # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify total price after increasing item quantity in cart successfully")
    def test_09_verify_increase_item_quantity_in_cart(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["sandwiches"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "large",
                                   "thin", m["Fries"], m["Additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            increase_item_in_cart(self.driver)
            time.sleep(2)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            print("Test case 09 ran successfully")
            # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify total price after decrease item quantity in cart successfully")
    def test_10_verify_decrease_item_quantity_in_cart(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["sandwiches"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "large",
                                   "thin", m["Fries"], m["Additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            increase_item_in_cart(self.driver)
            time.sleep(2)
            decrease_item_in_cart(self.driver)
            time.sleep(2)
            print("Test case 10 ran successfully")
            # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To change order setting from Delivery to Pickup at checkout page.")
    def test_11_Delivery_to_Pickup_order_setting(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(6)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            order_setting(self.driver, "Pickup")
            place_ur_order_from_payment(self.driver, "Pickup")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To change order setting from Pickup to Delivery at checkout page.")
    def test_12_Pickup_to_Delivery_order_setting(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            order_setting(self.driver, "Pickup")
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            order_setting(self.driver, "Delivery")
            place_ur_order_from_payment(self.driver, "Delivery")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify Recently placed order in order history.")
    def test_13_Verify_order_in_order_history(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["seafood_platters"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            self.driver.get("https://stage.bestintownpizza.com/home")
            time.sleep(6)
            order_history(self.driver, order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e


if __name__ == '__main__':

    unittest.main()
