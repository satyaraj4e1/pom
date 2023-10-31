import time

from selenium.webdriver.common.by import By
class LoginPage:
    # textbox_username_id = "Email"
    textbox_username_id="//input[@id='Email']"
    # textbox_username_id = "//input[@id='username']"
    textbox_password_id = "//input[@id='Password']"
    # textbox_password_id="password"
    button_login_xpath="//div/button[@class='button-1 login-button']"
    link_logout_linktext="//a[@href='/logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_id).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)
        # self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        # self.driver.find_element_by_id(self.textbox_password_id).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)
        # self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        # self.driver.find_element_by_xpath(self.button_login_xpath).click()
        time.sleep(20)
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_linktext).click()
        # self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        time.sleep(3)