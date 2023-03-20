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
from methods import order_setting, select_combo_item, verify_order_details, add_to_bag_and_verify_cart_details_combo


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


class TestMenuItems(TestBestInTownpizzabase):

    @allure.description("To verify that combo pizza are able to add to cart")
    def test_01_combo_pizzas(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
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

    @allure.description("To verify that seafood platters are able to add to cart")
    def test_02_seafood_platters(self):
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
                Checkout_to_paymentscreen(self.driver)
                time.sleep(3)
                place_ur_order_from_payment(self.driver, "Delivery")
                time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify that GOURMET PIZZA are able to add to cart")
    def test_03_gourmet_pizza(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["gourmet_pizza"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "large",
                                   "thin", m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
                Checkout_to_paymentscreen(self.driver)
                time.sleep(2)
                place_ur_order_from_payment(self.driver, "Delivery")
                time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify that stuffed pizza are able to add to cart")
    def test_04_stuffed_pizza(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["Stuffed Pizza"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "large",
                                   "thin", m["onion"], m["additional_topping"])
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

    @allure.description("To verify that strambolis are able to add to cart")
    def test_05_strambolies(self):
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

            Checkout_to_paymentscreen(self.driver)
            place_ur_order_from_payment(self.driver, "Delivery")
            time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify Calzones are able to add to cart")
    def test_06_Calzones(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["Calzones_menu"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            place_ur_order_from_payment(self.driver, "Delivery")
            time.sleep(2)

            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify buffalo wings are able to add to cart")
    def test_08_buffalo_wings(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["BUFFALO WINGS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                time.sleep(5)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
                time.sleep(2)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            print("Test case 07 ran successfully")
            # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify Hoagies_grinders added in cart successfully")
    def test_07_Hoagies_grinders(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["Hoagies_grinders"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_toppings(
                    self.driver, m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)

            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            print("Test case 07 ran successfully")
            # time.sleep(5)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify Steaks added in cart successfully")
    def test_09_Steaks(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["Steaks"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_toppings(
                    self.driver, m["additional_topping"], m["platter"])
                add_to_bag_and_verify_cart_details(self.driver)
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

    @allure.description("To verify Chicken Cheesesteaks added successfuly to cart.")
    def test_10_Chicken_Cheesesteaks(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(6)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["Chicken Cheesesteaks"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_toppings(
                    self.driver, m["additional_topping"], m["platter"])
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

    @allure.description("To verify SALMON STEAKS successfully added to cart.")
    def test_11_SALMON_STEAKS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            order_setting(self.driver, "Pickup")
            for m in data["SALMON STEAKS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
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

    @allure.description("To verify QUESADILLAS added successfully to cart.")
    def test_12_QUESADILLAS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["QUESADILLAS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify TRIPLE CLUBS added successfully to cart.")
    def test_13_TRIPLE_CLUBS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["TRIPLE_CLUBS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["bread"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify STEAMED SEAFOOD PLATTERS added successfully to cart.")
    def test_14_STEAMED_SEAFOOD_PLATTERS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["STEAMED_SEAFOOD_PLATTERS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["addon"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify ITALIAN PLATTERS added successfully to cart.")
    def test_15_ITALAIN_PLATTER(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["ITALIAN PLATTERS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["pasta"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify BURGERS added successfully to cart.")
    def test_16_Burgers(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["BURGERS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["extras"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify HOT PLATTERS added successfully to cart.")
    def test_17_Hot_Platter(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["HOT PLATTERS HALAL"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["extras"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify SANDWICHES HALAL added successfully to cart.")
    def test_18_SANDWICHES_HALAL(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["SANDWICHES HALAL"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["extras"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify SALAD HALAL MEDITERRAN added successfully to cart.")
    def test_19_SALAD_HALAL_SPECIALITY(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["SALAD HALAL"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["Dressing"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify APPETIZERS HALAL added successfully to cart.")
    def test_20_APPETIZERS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["APPETIZERS HALAL"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify DESSERTSL added successfully to cart.")
    def test_21_DESSERTS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["DESSERTS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify SIDE ORDERS added successfully to cart.")
    def test_22_SIDE_ORDERS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["SIDE ORDERS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verifyHOT SANDWICHES added successfully to cart.")
    def test_23_HOT_SANDWICHES(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["HOT SANDWICHES"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify COLD SANDWICHES added successfully to cart.")
    def test_24_COLD_SANDWICHES(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["COLD SANDWICHES"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify PANINIS added successfully to cart.")
    def test_25_PANINIS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["PANINIS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])

                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify WRAPS added successfully to cart.")
    def test_26_WRAPS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["WRAPS"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify SALAD_PLATTER added successfully to cart.")
    def test_27_SALAD_PLATTER(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["SALAD_PLATTER"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify BEVERAGES added successfully to cart.")
    def test_28_BEVERAGES(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            time.sleep(2)
            for m in data["BEVERAGES"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, m["size"],
                                   m["crust"], m["platter"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            time.sleep(3)
            place_ur_order_from_payment(self.driver, "Delivery")
            order_number = verify_order_details(
                self.driver, "Delivery", "9:30am")
            print(order_number)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("To verify that PIZZAs are able to add to cart")
    def test_29_PIZZAS(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["menulist_pizza"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_pizza_sides(self.driver, "medium",
                                   "thin", m["onion"], m["additional_topping"])
                add_to_bag_and_verify_cart_details(self.driver)

            Checkout_to_paymentscreen(self.driver)
            place_ur_order_from_payment(self.driver, "Delivery")
            time.sleep(2)
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e


if __name__ == '__main__':

    unittest.main()
