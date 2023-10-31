import time
import pytest
from selenium import webdriver
from pageObjects.loginpage import LoginPage
# import utilities.readProperties import ReadConfig
# import utilities.customLogger import LogGen
from utilities import XLUtils
class Test_002_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    path=".//testData/LoginData.xlsx"
    # baseURL = ReadConfig.getApplicationURL()
    # username="admin@yourstore.com"
    # password="admin"
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            assert True
        else:
            assert False






















