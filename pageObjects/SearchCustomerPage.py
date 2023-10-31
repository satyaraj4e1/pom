import time
from selenium.webdriver.common.by import By
class SearchCustomer():

    btnNewCustomer_xpath="//div/a[@href='/Admin/Order/List']"

    def __init__(self,driver):
        self.driver=driver

    def setUserNam(self):
        self.driver.find_element(By.XPATH,self.btnNewCustomer_xpath).click()
        time.sleep(3)

    # def searchCustomerByEmail(self,email):
    #     flag=False
    #     for r in range(1,self.getNoOfRows()+1):
    #         table=self.driver.find_element(By.XPATH, self.txtEmail_id)
    #         emailid=table.find_element(By.XPATH, self.txtEmail_id).text
    #         if emailid==email:
    #             flag=True
    #             break
    #         return flag