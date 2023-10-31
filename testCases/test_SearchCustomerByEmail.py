import time
import pytest
from selenium import webdriver
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.loginpage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
class Test_AddNewCustomer_002:
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    @pytest.mark.sanity
    def test_addNewCustomer(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        time.sleep(3)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(6)
        # self.lp.clickLogout()
        act_title=self.driver.title
        # self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.get_screenshot_as_file("C:/Users/satya/PycharmProjects/pom/Screenshots/test_homePageTitle.png")
            assert False
        time.sleep(6)
        self.lp = SearchCustomer(self.driver)
        self.lp.setUserNam()



