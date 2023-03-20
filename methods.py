from tkinter import E
from selenium import webdriver
import allure
import pytest
import time
import requests
import random
from datetime import date
from selenium.webdriver.common.keys import Keys
from locators import loginlocators, ordertypeselectors, productlocators, checkoutlocators, menugroupLocators, cartLocators, paymentLocators, placedPaymentLocators
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType


@allure.step("To fetch the website with url: {1}")
def fetching_website(driver, site_url):
    try:
        driver.get(site_url)
        # driver.maximize_window()
        driver.set_window_size(1536, 864)
        driver.implicitly_wait(5)
        print(driver.title)
        allure.attach(driver.get_screenshot_as_png(),
                      name='website_screen', attachment_type=AttachmentType.PNG)
        try:
            driver.find_element_by_id(
                loginlocators.start_button).click()
        except:
            print("Restuarant has opened now")
        assert driver.title == "Home | Best In Town Pizzas"

    except Exception as e:
        raise e


def find_element_by_text(driver, element_text):
    item = driver.find_element_by_xpath(
        "//*[contains(text(),'{}')]".format(element_text))
    return item


def find_element_by_text2(driver, element_text):
    item = driver.find_element_by_xpath(
        "//a[text()='{}']".format(element_text))
    return item


def execute_click_by_product(driver, itemlist):
    try:
        item = product_click(driver, itemlist["menugroup"])
        time.sleep(3)
    except Exception as e:
        raise e


def future_date(driver):
    try:
        today = date.today()
        today = str(today)
        day = today[8:]
        order_date = int(day)+7
        print(order_date)
        return order_date
    except Exception as e:
        raise e


@allure.step("To perform click operation on the element specified in list:{1}")
def product_click(driver, productname):
    By_xpath = driver.find_element_by_xpath
    By_xpath_elements = driver.find_elements_by_xpath
    try:
        if productname == "Combo":
            By_xpath(menugroupLocators.combo).click()
        elif productname == "Pizza":
            By_xpath(menugroupLocators.pizza).click()
        elif productname == "GOURMET PIZZA":
            By_xpath(menugroupLocators.gourmet_Pizza).click()
        elif(productname == "Stuffed Pizza"):
            By_xpath(menugroupLocators.stuffed_Pizza).click()
        elif productname == "STROMBOLIS":
            By_xpath(menugroupLocators.strombolis).click()
        elif productname == "Calzones":
            By_xpath(menugroupLocators.calzones).click()
        elif productname == "Buffalo Wings":
            By_xpath(menugroupLocators.buffalo_wings).click()
        elif productname == "Steaks":
            By_xpath(menugroupLocators.steaks).click()
        elif productname == "Chicken Cheesesteaks":
            By_xpath(menugroupLocators.chicken_steaks).click()
        elif productname == "SALMON STEAKS":
            By_xpath(menugroupLocators.salmon_steaks).click()
        elif productname == "STEAMED SEAFOOD PLATTERS":
            By_xpath(menugroupLocators.seafood_platter).click()
        elif productname == "ITALIAN PLATTERS":
            By_xpath(menugroupLocators.italian_platter).click()
        elif productname == "BURGERS":
            By_xpath(menugroupLocators.burgers).click()
        elif productname == "QUESADILLAS":
            By_xpath(menugroupLocators.quesadillas).click()
        elif productname == "TRIPLE_CLUBS":
            By_xpath(menugroupLocators.triple_clubes).click()
        elif productname == "HOT PLATTERS":
            By_xpath(menugroupLocators.hot_Platters).click()
        elif productname == "SANDWICHES HALAL":
            By_xpath(menugroupLocators.sandwiches).click()
        elif productname == "SALAD HALAL":
            By_xpath(menugroupLocators.salad).click()
        elif productname == "DESSERTS":
            By_xpath(menugroupLocators.dessert).click()
        elif productname == "APPETIZERS":
            By_xpath(menugroupLocators.appetizers).click()
        elif productname == "SIDE ORDERS":
            By_xpath(menugroupLocators.side_orders).click()
        elif productname == "HOT SANDWICHES":
            By_xpath(menugroupLocators.hot_sandwiches).click()
        elif productname == "COLD SANDWICHES":
            By_xpath(menugroupLocators.cold_sandwiches).click()
        elif productname == "PANINIS":
            By_xpath(menugroupLocators.pannis).click()
        elif productname == "WRAPS":
            By_xpath(menugroupLocators.wraps).click()
        elif productname == "SALAD_PLATTER":
            By_xpath(menugroupLocators.salad_platters).click()
        elif productname == "FRIED SEAFOOD PLATTERS":
            By_xpath(menugroupLocators.fried_seafood).click()
        elif productname == "BEVERAGES":
            By_xpath(menugroupLocators.beverages).click()
        else:
            By_xpath(menugroupLocators.hoagies_grinders).click()
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='exceptionerror_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select desired product")
def select_product(driver, productname):
    By_xpath = driver.find_element_by_xpath
    By_list_xpath = driver.find_elements_by_xpath
    try:
        print(productname)
        productname1 = productname.upper()
        product = find_element_by_text(driver, productname)
        product.click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@allure.step("To be able to select desired product")
def select_combo_item(driver, size):
    By_xpath = driver.find_element_by_xpath
    By_list_xpath = driver.find_elements_by_xpath
    try:
        a = 0
        while(a < 6):
            try:
                time.sleep(2)
                find_element_by_text(driver, size).click()
            except:
                print("no size")
            try:
                try:
                    driver.find_element_by_xpath(
                        productlocators.beef_peproni).click()
                except:
                    try:
                        driver.find_element_by_xpath(
                            productlocators.hot_pepper).click()
                    except:
                        try:
                            driver.find_element_by_xpath(
                                productlocators.soda_can).click()
                        except:
                            driver.find_element_by_xpath(
                                productlocators.italian_dressing).click()

            except:

                try:
                    driver.find_element_by_id(
                        productlocators.product_instruction).send_keys("No Pickels")
                except:
                    try:
                        driver.find_element_by_id(
                            productlocators.product_instructions).send_keys("No instructions")
                    except:
                        driver.find_element_by_id(
                            productlocators.product_instructions3).send_keys("Make it fast")
            try:
                driver.find_element_by_xpath(productlocators.next_btn).click()
            except:
                print("now add to bag")
                break
            time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        print("product")
    except Exception as e:
        raise e


@allure.step("To check website availability")
def is_website_available(driver, url):
    try:
        request_response = requests.head(url)
        status_code = request_response.status_code
        website_is_up = status_code == 200
        print("website_is_up")
        allure.attach(driver.get_screenshot_as_png(),
                      name='Website_screen', attachment_type=AttachmentType.PNG)
    except Exception as ex:
        raise ex


@allure.step("To create a new account")
def sign_up(driver, firstname, email, password, confirmpassword):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_xpath(loginlocators.signup_btn).click()
        time.sleep(2)
        By_id(loginlocators.signup_name).send_keys(firstname)
        By_id(loginlocators.signup_email).send_keys(email)
        By_id(loginlocators.signup_password).send_keys(password)
        By_id(loginlocators.signup_confirmPassword).send_keys(confirmpassword)
        By_xpath(loginlocators.register_btn).click()
        time.sleep(7)
        try:
            heading = By_xpath(loginlocators.home_signin_btn).text
            print(heading)
            assert firstname in heading
        except:
            print("error is there")
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Signup_failure_screen', attachment_type=AttachmentType.PNG)
        raise ex


@allure.step("To verify that user is able to sign in with any email id.")
def sign_in(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_id(loginlocators.signin_email).send_keys(email)
        By_id(loginlocators.signin_password).send_keys(password)
        By_xpath(loginlocators.signin_btn).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        signed_in = By_xpath(loginlocators.signedin_label).text
        print(signed_in)
        assert signed_in in "RITU"
        return signed_in

    except Exception as e:
        raise e


@allure.step("To verify that user is able to sign in with Bestintown pizza account")
def forget_password_link(driver, email):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(1)
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_xpath(loginlocators.forget_password_btn).click()
        time.sleep(1)
        By_xpath(loginlocators.forget_password_email_field).send_keys(email)
        time.sleep(1)
        By_xpath(loginlocators.reset_link_btn).click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        success_msg = By_xpath(loginlocators.success_msg).text
        assert success_msg == "We have e-mailed your password reset link!"
        time.sleep(2)
    except Exception as e:
        raise e


@allure.step("To verify that user is able to sign in with Bestintown pizza account")
def sign_in2(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(1)
        By_xpath(loginlocators.signin_email).send_keys(email)
        By_xpath(loginlocators.signin_password).send_keys(password)
        By_xpath(loginlocators.signin_btn).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        time.sleep(2)
    except Exception as e:
        raise e


@allure.step("To edit profile information")
def edit_profile(driver, name, email, name2):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(2)
        By_xpath(loginlocators.signedin_label).click()
        time.sleep(3)
        By_xpath(loginlocators.profile_btn).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(
        ), name='updated profile screen1', attachment_type=AttachmentType.PNG)
        time.sleep(2)
    except Exception as e:
        raise e


@allure.step("To add delivery address")
def add_delivery_address(driver, hno):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        time.sleep(5)
        By_xpath(loginlocators.signedin_label).click()
        time.sleep(3)
        By_xpath(loginlocators.del_add_link).click()
        time.sleep(4)
        By_xpath(loginlocators.add_new_address_btn).click()
        time.sleep(2)
        By_xpath(loginlocators.new_add_field).send_keys(hno)
        time.sleep(3)
        By_xpath(loginlocators.new_add_field).send_keys(Keys.DOWN)
        By_xpath(loginlocators.new_add_field).send_keys(Keys.ENTER)
        try:
            warning_msg = By_xpath(loginlocators.warning_msg).text
            assert warning_msg == "The Address already exists."
            # By_xpath(loginlocators.ok_btn).click()
            success_msg = By_xpath(loginlocators.address_add_message).text
            print(success_msg)
            assert success_msg == "Good news! Best In Town Pizzas can deliver to this address"
            By_xpath(loginlocators.close_btn).click()
        except:
            print("new address ha sbeen added")
            allure.attach(driver.get_screenshot_as_png(
            ), name='new_updated_address', attachment_type=AttachmentType.PNG)
            time.sleep(2)
        address_table = By_xpath(loginlocators.address_table).text
        time.sleep(1)
        assert hno in address_table
    except Exception as e:
        raise e


@allure.step("To login and then logout of the account")
def logout(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(3)
        By_xpath(loginlocators.logout_link).click()
        time.sleep(6)
    except Exception as e:
        raise e


@allure.step("To verify that user is able to sign in withwrong credientials")
def invalid_signin(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_id(loginlocators.signin_email).send_keys(email)
        By_id(loginlocators.signin_password).send_keys(password)
        By_xpath(loginlocators.signin_btn).click()
        time.sleep(1)
        error = By_xpath(loginlocators.error_msg).text
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        print(error)
        err_msg = "These credentials do not match our records."
        assert err_msg in error
    except Exception as e:
        raise e


@allure.step("To be able to select pizza sides and quantity")
def select_pizza_sides(driver, size, crust, onions, additional_Topping):
    By_xpath = driver.find_element_by_xpath
    try:
        try:
            if size == "medium":
                By_xpath(productlocators.pizza_large_size).click()

            elif size == "large":
                By_xpath(productlocators.pizza_large_size).click()
            else:
                try:
                    By_xpath(productlocators.pizza_Xlarge_size).click()
                except:
                    By_xpath(productlocators.stuffd_pizza_Xlarge_size).click()
        except Exception as ex:
            print("no size selected")
            raise ex
        try:
            if crust == "regular":
                By_xpath(productlocators.pizza_crust_regulr).click()
            elif crust == "thin":
                By_xpath(productlocators.pizza_crust_thin).click()
            else:
                print("no crust")
        except Exception as es:
            print("no crust2")
    except:
        print("nothing")
    try:
        try:
            item = By_xpath(
                "//*[contains(text(),'{}')]/ancestor::label//ancestor::div//ancestor::div//ancestor::div/div[1]/div/label/div[1]/span[1]".format(onions))

        except:
            try:
                item = By_xpath(
                    "/html/body/div[8]/div/div/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/span[1]")
            except:
                try:
                    item = By_xpath(
                        "/html/body/div[8]/div/div/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div/label/div[1]/span[1]")
                except:
                    item = By_xpath(
                        "/html/body/div[8]/div/div/div/div/div/div[2]/div[3]/div[1]/div[3]/div[2]/div[1]/div/label/div[1]/span[1]")
        time.sleep(2)
        item.click()

        try:
            style = By_xpath(menugroupLocators.style)
            time.sleep(2)
            style.click()
        except:
            print("no style no dressing")
    except:
        print("No Toppings")
    allure.attach(driver.get_screenshot_as_png(),
                  name='toppings_screen', attachment_type=AttachmentType.PNG)
    time.sleep(4)


@allure.step("To be able to select desired quantity")
def select_toppings(driver, platter, topping):
    try:
        By_xpath = driver.find_element_by_xpath
        try:

            # item = By_xpath(
            #     "//*[contains(text(),'{}')]/ancestor::div//ancestor::div//ancestor::div//ancestor::div/div[1]/div/label/div[1]/span[1]".format(platter))

            # item.click()
            try:
                item2 = By_xpath(
                    "//*[contains(text(),'())')]/ancestor::div//ancestor::div//ancestor::div//ancestor::div/div[1]/div/label/div[1]/span[1]".format(topping))
                item2.click()
            except:
                item22 = By_xpath(
                    "//*[contains(text(),'{}')]/ancestor::div//ancestor::div//ancestor::div//ancestor::div/div/div[1]/span[1]".format(platter))
                item22.click()
            try:
                item3 = By_xpath(
                    "//*[contains(text(),'YES')]/ancestor::label//ancestor::div//ancestor::div//ancestor::div/div[1]/div/label/div[1]/span[1]")
                item3.click()
            except:
                print("no grinder")
        except Exception as ex:
            allure.attach(driver.get_screenshot_as_png(),
                          name='toppings_screen_failure', attachment_type=AttachmentType.PNG)
            raise ex

    except Exception as e:
        raise e


@allure.step("to add product to bag and verify cart details before checkout")
def add_to_bag_and_verify_cart_details(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        try:
            By_xpath(productlocators.add_to_bag_btn_price).click()
        except:
            By_xpath(productlocators.add_to_bag_btn2).click()
        time.sleep(3)
        driver.execute_script("window.scroll(0, 0)")
        print("scroll up")
        time.sleep(4)
        By_xpath(cartLocators.cart_bag).click()
        time.sleep(5)
        item_price = By_xpath(cartLocators.product_price).text
        print("product price:  " + item_price)
        item_price2 = item_price[1:]
        print(item_price2)

        subtotal = By_xpath(cartLocators.cart_subtotal).text
        subtotal2 = subtotal[1:]
        print(subtotal2)

        dis = By_xpath(cartLocators.discount).text
        dis_amount = dis[1:]
        print(dis_amount)
        try:
            fee = By_xpath(cartLocators.delivery_fee).text
            delivery_fee = fee[1:]
            print(delivery_fee)
        except:
            print("its a pickup order")

        try:
            tax = By_xpath(cartLocators.estimated_tax).text
            tax2 = tax[1:]
            print(tax2)
            totalprice = float(subtotal2) + float(delivery_fee) + \
                float(dis_amount) + float(tax2)
            print(totalprice)
        except:
            print("no discount")
            try:
                totalprice = float(subtotal2) + \
                    float(delivery_fee) + float(dis_amount)
            except:
                totalprice = float(subtotal2) + float(dis_amount)
            print(totalprice)
        format_float = "{:.2f}".format(totalprice)
        try:
            total = By_xpath(cartLocators.total).text
            time.sleep(1)
        except:
            try:
                total = By_xpath(cartLocators.total1).text
                time.sleep(1)
            except:
                total = By_xpath(cartLocators.total2).text
                time.sleep(1)
        total2 = total[1:]
        total3 = float(total2)
        format_float2 = "{:.2f}".format(total3)
        print(total3)
        assert format_float2 == format_float

        print("added to bag")
        allure.attach(driver.get_screenshot_as_png(),
                      name='cart_screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("to add product to bag and verify cart details before checkout")
def add_to_bag_and_verify_cart_details_combo(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        try:
            By_xpath(productlocators.add_to_bag_btn_price).click()
        except:
            By_xpath(productlocators.add_to_bag_btn2).click()
        time.sleep(2)

        By_xpath(cartLocators.cart_bag).click()
        time.sleep(5)

        item_price = By_xpath(cartLocators.product_price).text
        print("product price:  " + item_price)
        item_price2 = item_price[1:]
        print(item_price2)

        subtotal = By_xpath(cartLocators.cart_subtotal).text
        subtotal2 = subtotal[1:]
        print(subtotal2)

        dis = By_xpath(cartLocators.discount).text
        dis_amount = dis[3:]
        print(dis_amount)
        try:
            fee = By_xpath(cartLocators.delivery_fee).text
            delivery_fee = fee[1:]
            print(delivery_fee)
        except:
            print("its a pickup order")

        tax = By_xpath(cartLocators.estimated_tax).text
        tax2 = tax[1:]
        print(tax2)
        try:
            totalprice = float(subtotal2) + float(delivery_fee) - \
                float(dis_amount) + float(tax2)
            print(totalprice)
        except:
            totalprice = float(subtotal2) + \
                float(delivery_fee) - float(dis_amount)
            print(totalprice)
        format_float = "{:.2f}".format(totalprice)
        try:
            total = By_xpath(cartLocators.total).text
            time.sleep(1)
        except:
            try:
                total = By_xpath(cartLocators.total1).text
                time.sleep(1)
            except:
                total = By_xpath(cartLocators.total2).text
                time.sleep(1)
        total2 = total[1:]
        total3 = float(total2)
        format_float2 = "{:.2f}".format(total3)
        print(total3)
        assert format_float2 == format_float

        print("added to bag")
        allure.attach(driver.get_screenshot_as_png(),
                      name='cart_screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@ allure.step("To verify increment of the item quantity and price details in cart")
def increase_item_in_cart(driver):
    By_xpath = driver.find_element_by_xpath
    try:

        By_xpath(cartLocators.cart_increment_btn).click()
        time.sleep(2)
        By_xpath(cartLocators.cart_increment_btn).click()
        time.sleep(2)
        print("item increased")

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@ allure.step("To verify decrement of the item quantity and price details in cart")
def decrease_item_in_cart(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        # get details before decrement the item quantity
        By_xpath(cartLocators.cart_decrement_btn).click()
        time.sleep(2)
        By_xpath(cartLocators.cart_decrement_btn).click()
        time.sleep(2)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@ allure.step("edit items")
def edit_items(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        try:
            By_xpath(cartLocators.edit_btn).click()
        except:
            By_xpath(cartLocators.edit_btn2).click()
        time.sleep(3)
        By_id(productlocators.product_instruction).clear()
        By_id(productlocators.product_instruction).send_keys(
            "Send Pickles and extra toppings")
        try:
            By_id(cartLocators.increase_qty).click()
            By_id(cartLocators.increase_qty).click()
        except:
            By_xpath(
                "/html/body/div[8]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div/div[2]/div[2]/div/label/div[1]/span[1]").click()

    except Exception as ex:
        raise ex


@allure.step("empty cart")
def delete_items_empty_cart(driver):
    By_xpath = driver.find_element_by_xpath
    no_of_items = By_xpath(cartLocators.item_number).text
    no_of_items = no_of_items[0]
    print(no_of_items)
    no_of_items = int(no_of_items)
    try:
        while no_of_items > 0:
            By_xpath(cartLocators.delete_item).click()
            By_xpath(cartLocators.remove_btn).click()
            print("item deleted")
            try:
                heading = By_xpath(cartLocators.empty_cart_headng).text
                print(heading)
                assert heading == "YOUR BAS IS EMPTY."

            except:
                no_of_items = By_xpath(cartLocators.item_number).text
                no_of_items = no_of_items[0]
                print(no_of_items)
                no_of_items = int(no_of_items)
        try:
            tax = By_xpath(cartLocators.estimated_tax2).text
            time.sleep(1)
            assert tax in "$0.00"
        except:
            print("no delivery fee in pickup")
        time.sleep(1)
        checkout = By_xpath(cartLocators.checkout_price).text
        time.sleep(1)
        assert checkout in "$0.00"
    except Exception as ex:
        raise ex


@ allure.step("Checkout to payment screen")
def Checkout_to_paymentscreen(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(cartLocators.checkout_btn).click()
        time.sleep(3)
        cart_heading1 = By_xpath(paymentLocators.cart_summary_hedng).text
        time.sleep(2)
        assert cart_heading1 in "CART SUMMARY"
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To add a new Delivery Address at checkout stage.")
def add_new_del_add(driver, address):
    By_xpath = driver.find_element_by_xpath
    By_name = driver.find_element_by_name
    try:
        try:
            By_xpath(checkoutlocators.plus_add_address1).click()
        except:
            try:
                By_xpath(checkoutlocators.plus_add_address).click()
            except:
                By_xpath(checkoutlocators.plus_add_address2).click()
        By_xpath(checkoutlocators.new_address_bar).send_keys(address)
        time.sleep(1)
        By_xpath(checkoutlocators.new_address_bar).send_keys(Keys.DOWN)
        By_xpath(checkoutlocators.new_address_bar).send_keys(Keys.ENTER)
        # By_xpath(checkoutlocators.save_this_address_btn).click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
        time.sleep(7)
        address_list = driver.find_elements_by_xpath(
            checkoutlocators.address_list)
        print(address)
        for i in address_list:
            print(i.text)
            assert address in i.text
    except Exception as e:
        raise e


@ allure.step("To remove a Delivery Address at checkout stage.")
def remove_del_add(driver, address):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(checkoutlocators.remove_add_btn).click()
        time.sleep(2)
        By_xpath(checkoutlocators.remove_ok_btn).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        raise e


@ allure.step("To edit a existing Delivery Address at checkout stage.")
def edit_del_add(driver, hno):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(checkoutlocators.edit_add_btn).click()
        By_xpath(checkoutlocators.edit_hno_field).clear()
        By_xpath(checkoutlocators.edit_hno_field).send_keys(hno)
        time.sleep(1)
        By_xpath(checkoutlocators.save_this_address_btn).click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
        time.sleep(7)
        address_list = driver.find_elements_by_xpath(
            checkoutlocators.address_list)
        for i in address_list:
            print(i.text)
            assert hno in i.text
    except Exception as e:
        raise e


@ allure.step("To add new card")
def add_new_card(driver, name, number, month, year, cvc):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        try:
            By_xpath(checkoutlocators.plus_card_details).click()
        except:
            By_xpath(checkoutlocators.plus_card_details2).click()
        time.sleep(2)
        By_xpath(checkoutlocators.card_owner_name).send_keys(name)
        By_xpath(checkoutlocators.new_card_number).send_keys(number)
        Select(By_xpath(checkoutlocators.new_expiry_month)
               ).select_by_visible_text(month)
        Select(By_xpath(checkoutlocators.new_expiry_year)
               ).select_by_visible_text(year)
        By_xpath(checkoutlocators.new_cvc).send_keys(cvc)
        By_xpath(checkoutlocators.billing_address).send_keys(
            "30 Hudson yards, NY, USA")
        By_xpath(checkoutlocators.save_card_btn).click()
        time.sleep(5)
        print(name)
        time.sleep(5)
        card_list = driver.find_elements_by_xpath(
            checkoutlocators.card_list)
        for i in card_list:
            print(i.text)
            assert name in i.text
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(
        ), name='card_screen_failure', attachment_type=AttachmentType.PNG)
        raise ex


@ allure.step("To remove a saved card at checkout stage.")
def remove_saved_card(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        By_xpath(checkoutlocators.remove_card_btn).click()
        time.sleep(2)
        try:
            By_xpath(checkoutlocators.remove_card_ok).click()
        except:
            By_xpath(checkoutlocators.remove_card_ok2).click()
        time.sleep(4)
        try:
            By_xpath(checkoutlocators.ok_success_btn).click()
        except:
            By_xpath(checkoutlocators.ok_success_btn2).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        raise e


@allure.step("palace your order")
def place_ur_order_from_payment(driver, status):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(3)
        cart_heading1 = By_xpath(paymentLocators.cart_summary_hedng).text
        time.sleep(2)
        assert cart_heading1 in "CART SUMMARY"
        time.sleep(2)
        if status == "Delivery":
            By_xpath(paymentLocators.select_delivery_address).click()
            time.sleep(2)
        else:
            print("Pickup order")
        By_xpath(paymentLocators.payment_card).click()
        time.sleep(2)
        By_xpath(paymentLocators.palce_ur_ordr).click()
        time.sleep(2)

        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@allure.step("To change order setting to Pickup option")
def order_setting(driver, order_type):
    By_xpath = driver.find_element_by_xpath
    try:
        if order_type == "Pickup":
            By_xpath(checkoutlocators.pickup_path).click()
        else:
            By_xpath(checkoutlocators.delivery_path).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(
        ), name='order_setting_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To verify order details after order placement")
def verify_order_details(driver, order_type, timeslot):
    By_xpath = driver.find_element_by_xpath
    try:
        order_status = By_xpath(placedPaymentLocators.order_status).text
        order_number = By_xpath(placedPaymentLocators.order_number).text
        assert order_type in order_status
        print("order_type matched")
        allure.attach(driver.get_screenshot_as_png(
        ), name='final_order_setting_screen', attachment_type=AttachmentType.PNG)
        return order_number
    except Exception as e:
        raise e


@ allure.step("To change order setting to Delivery option")
def asap_setting(driver, address):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.del_link_path).click()
        time.sleep(2)
        Select(By_xpath(productlocators.address_field)).select_by_value(address)
        allure.attach(driver.get_screenshot_as_png(
        ), name='asap_order_setting_screen', attachment_type=AttachmentType.PNG)
        time.sleep(3)
        By_xpath(productlocators.change_date_time_path).click()
        time.sleep(2)
        By_xpath(loginlocators.asap_btn).click()
        time.sleep(2)
        By_xpath(loginlocators.now_btn).click()
        time.sleep(2)
        # order_label=By_xpath(productlocators.order_label).text
        # print(order_label)
        # assert "ASAP" in order_label
    except Exception as e:
        raise e


@allure.step("Later order setting to Delivery option")
def later_order_setting(driver, order_time):
    By_xpath = driver.find_element_by_xpath
    try:
        order_date = future_date(driver)
        By_xpath(ordertypeselectors.calender).click()
        By_xpath(ordertypeselectors.later).click()
        cal_dates = driver.find_elements_by_xpath(
            "//*[@class='datepicker--cell datepicker--cell-day']")

        for i in cal_dates:
            print("in for11")
            print(i.text)
            if i.get_attribute("data-date") == str(order_date):
                i.click()
                break
        By_xpath(ordertypeselectors.select_time).click()
        time.sleep(1)
        available_time = driver.find_elements_by_xpath(
            "//*[@class='ui-menu-item']")
        for i in available_time:
            if i.text == (order_time):
                i.click()
                break
        time.sleep(2)
        By_xpath(ordertypeselectors.save_time).click()
        time.sleep(5)
        later_date = By_xpath(ordertypeselectors.calender).text
        print(later_date)
        assert str(order_time) in later_date
        assert str(order_date) in later_date
    except Exception as e:
        raise e


@allure.step("Later order setting to Delivery option")
def today_order_setting(driver, order_time):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(ordertypeselectors.calender).click()
        try:
            By_xpath(ordertypeselectors.select_time).click()
        except:
            By_xpath(ordertypeselectors.today_select_time).click()
            time.sleep(1)
        available_time = driver.find_elements_by_xpath(
            "//*[@class='ui-menu-item']")
        for i in available_time:
            if i.text == (order_time):
                i.click()
                break
        time.sleep(2)
        By_xpath(ordertypeselectors.save_time).click()
        time.sleep(5)
        order_date_time = By_xpath(ordertypeselectors.calender).text
        print(order_date_time)
        assert str(order_time) in order_date_time
    except Exception as e:
        raise e


@ allure.step("To add a customise tip from customer")
def custom_tip(driver, tip):
    By_xpath = driver.find_element_by_xpath
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        By_xpath(checkoutlocators.custome_tip_btn).click()
        time.sleep(2)
        By_xpath(checkoutlocators.tip_xpath).clear()
        time.sleep(5)
        By_xpath(checkoutlocators.tip_xpath).send_keys("3")
        time.sleep(6)
        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To add tip according to percentage")
def fix_tip(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.percent_tip).click()
    except Exception as ex:
        raise ex

@ allure.step("To verify get contact us info")
def get_contactus_info(driver):
    By_xpath = driver.find_element_by_xpath
    try:

        By_xpath(loginlocators.contact_us).click()
        time.sleep(2)
        heading1 = By_xpath(loginlocators.aboutus_heading).text
        print(heading1)
        assert heading1 in "ABOUT BEST IN TOWN PIZZAS"
        heading = By_xpath(loginlocators.openhours_heading).text
        assert heading in "BUSINESS HOURS"
        open_days = By_xpath(loginlocators.opendays).text
        assert open_days in "Monday - Saturday"
        open_hrs = By_xpath(loginlocators.openhours).text
        assert open_hrs in "9:00AM - 9:00PM"
        closeday = By_xpath(loginlocators.close_days).text
        assert closeday in "Sunday"
        close = By_xpath(loginlocators.close_text).text
        assert close in "Closed"
        partial_day = By_xpath(loginlocators.partialday).text
        assert partial_day in "Friday"
        time.sleep(2)
        By_xpath(loginlocators.arrow).click()
        time.sleep(2)
        top_headings = By_xpath(loginlocators.top_heading).text
        assert top_headings in "BEST IN TOWN PIZZAS"
    except Exception as e:
        raise e

@allure.step("To check the order in order history")
def order_history(driver, order_number):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(2)
        By_xpath(placedPaymentLocators.order_history_btn).click()
        time.sleep(2)
        order_num = By_xpath(placedPaymentLocators.order_number_in_list).text
        assert order_number in order_num
    except Exception as e:
        raise e
