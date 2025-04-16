# Importing the necessary Selenium WebDriver module to control web browsers
import time

from selenium import webdriver
# Importing specific element locating strategies from Selenium's WebDriver module
from selenium.webdriver.common.by import By


# Creating a Login class for handling login functionality
class Login:
    # Storing locators for elements on the login page
    text_box_username_Name = "username"  # Locator for the username text box using the 'name' attribute
    text_box_password_Name = "password"  # Locator for the password text box using the 'name' attribute
    btn_login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'  # XPath for the login button

    # Initializing the Login class with a WebDriver instance
    def __init__(self, driver):
        self.driver = driver

    # Method to set the username in the username text box
    def setUsername(self, username):
        # Finding the username element by its name, clearing any existing text, and entering the provided username
        self.driver.find_element(By.NAME, self.text_box_username_Name).clear()
        self.driver.find_element(By.NAME, self.text_box_username_Name).send_keys(username)

    # Method to set the password in the password text box
    def setPassword(self, password):
        # Finding the password element by its name, clearing any existing text, and entering the provided password
        self.driver.find_element(By.NAME, self.text_box_password_Name).clear()
        self.driver.find_element(By.NAME, self.text_box_password_Name).send_keys(password)

    # Method to perform a click action on the login button
    def clickLogin(self):
        # Locating the login button by its XPath and clicking it to initiate the login process
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

class Leave:
    leave_title_xpath = "//h6[text()='Leave']"
    my_leave_icon_xpath = "//span[text()='My Leave']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyLeave(self):
        self.driver.find_element(By.XPATH, self.leave_title_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.my_leave_icon_xpath).click()

class Logout:
    profile_icon_xpath = "//img[@alt='profile picture']"
    logout_button_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.profile_icon_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()




