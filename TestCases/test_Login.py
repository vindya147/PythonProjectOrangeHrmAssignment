# Importing the pytest library for test framework functionalities
import pytest
# Importing the webdriver module from Selenium for browser automation
from selenium import webdriver
# Importing the Login class from the Login_pg module under the Pages package
#from PageObjects.Loginpg import Login
from PageObjects.Loginpg import Login, Logout, Leave
# Importing the time module for time-related operations
import time




# Defining a test class named Test_001_Login
class Test_001_Login:
    # Declaring class-level variables for base URL, username, and password
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Test method to verify the home page title
    def test_LoginpageTitle(self):
        # Initiating a Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 5 seconds to ensure page loads completely
        time.sleep(5)

        # Getting the title of the current page
        act_title = self.driver.title

        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title matches the expected title
        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")

    # Test method to perform login functionality
    def test_login(self):
        # Initiating another Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Creating an instance of the Login class by passing the driver instance
        self.lp = Login(self.driver)

        # Setting the username in the login page
        self.lp.setUsername(self.username)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Setting the password in the login page
        self.lp.setPassword(self.password)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Clicking the login button in the login page
        self.lp.clickLogin()

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Getting the title of the current page
        act_title = self.driver.title

        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title matches the expected title on Home page
        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")

    def test_logout(self):
        # Initiating another Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Creating an instance of the Login class by passing the driver instance
        self.lp = Login(self.driver)

        # Setting the username in the login page
        self.lp.setUsername(self.username)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Setting the password in the login page
        self.lp.setPassword(self.password)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Clicking the login button in the login page
        self.lp.clickLogin()

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Creating an instance of the logout class by passing the driver instance
        self.lp = Logout(self.driver)

        # clicking the logout button in the page
        self.lp.clickLogout()

        # pausing execution for  3 seconds
        time.sleep(3)

        # Getting the title of the current page
        act_title = self.driver.title

        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title matches the expected title on Home page
        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")

    def test_Leaving(self):
        # Initiating another Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Creating an instance of the Login class by passing the driver instance
        self.lp = Login(self.driver)

        # Setting the username in the login page
        self.lp.setUsername(self.username)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Setting the password in the login page
        self.lp.setPassword(self.password)

        # Pausing execution for 3 seconds
        time.sleep(3)

        # Clicking the login button in the login page
        self.lp.clickLogin()

        # Pausing execution for 3 seconds
        time.sleep(3)

        self.lp = Leave(self.driver)

        # clicking the myleaving button in the page
        self.lp.clickMyLeave()

        # pausing execution for  3 seconds
        time.sleep(3)

        # Getting the title of the current page
        act_title = self.driver.title

        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title matches the expected title on Home page
        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")





