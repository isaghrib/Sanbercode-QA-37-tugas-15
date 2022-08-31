from cgitb import text
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestRegisterFail(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_failed_register_using_email_registered(self):
        #steps
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email_create").send_keys("isaghrib@aziz.com")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitCreate").click()
        time.sleep(5)

        #validation
        text_registered = browser.find_element(By.ID, "create_account_error").text

        self.assertIn('registered', text_registered)
    
    def test_b_failed_format_email_register(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email_create").send_keys("isaghrib")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitCreate").click()
        time.sleep(5)

        text_invalid_email = browser.find_element(By.CSS_SELECTOR, "div#create_account_error.alert.alert-danger").text
        
        self.assertIn("Invalid email", text_invalid_email)
    
    def tearDown(self):
        self.browser.close()

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email").send_keys("isaghrib@aziz.com")
        time.sleep(1)
        browser.find_element(By.ID, "passwd").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitLogin").click()
        time.sleep(5)

        text_header = browser.find_element(By.ID, "center_column").text
        text_body = browser.find_element(By.CSS_SELECTOR, "p.info-account").text

        self.assertIn("Welcome", text_body)
        self.assertIn("MY ACCOUNT", text_header)

    def test_b_failed_login_invalid_email(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email").send_keys("isaghrib")
        time.sleep(1)
        browser.find_element(By.ID, "passwd").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitLogin").click()
        time.sleep(5)

        text_header = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text

        self.assertIn("error", text_header, "not same")
        self.assertIn("Invalid email address.", text_header, "not same")

    def test_c_failed_login_invalid_password(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email").send_keys("isaghrib@aziz.com")
        time.sleep(1)
        browser.find_element(By.ID, "passwd").send_keys("qwerty")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitLogin").click()
        time.sleep(5)

        text_header = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text

        self.assertIn("error", text_header, "not same")
        self.assertIn("Authentication failed.", text_header, "not same")

    def test_d_failed_login_email_and_password_blank(self):
        #steps
        browser = self.browser
        browser.get(
            "http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(3)
        browser.find_element(By.ID, "SubmitLogin").click()
        time.sleep(5)

        #validation
        text_registered = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text

        self.assertIn('error', text_registered)
        self.assertIn('required', text_registered)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
