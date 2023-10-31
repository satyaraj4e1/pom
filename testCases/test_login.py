import time
import pytest
from selenium import webdriver
from pageObjects.loginpage import LoginPage
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.save_screenshot("C:.//Users//satya//PycharmProjects//pom//Screenshots//test_homePageTitle.PNG")
        self.driver.get_screenshot_as_file("C:/Users/satya/PycharmProjects/pom/Screenshots/test_homePageTitle.png")
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False

    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        time.sleep(5)
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
            assert False
        self.lp.clickLogout()
