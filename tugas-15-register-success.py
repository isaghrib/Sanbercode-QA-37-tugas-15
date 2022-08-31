from cgitb import text
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterSuccess(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register(self):
        #steps
        browser = self.browser
        browser.get("https://automationpractice.com/")
        time.sleep(5)
        browser.find_element(By.CLASS_NAME,"login").click()
        time.sleep(3)
        browser.find_element(By.ID,"email_create").send_keys("isaghrib@aziz.com")
        time.sleep(1)
        browser.find_element(By.NAME,"SubmitCreate").click()
        time.sleep(3)
        #Personal Information
        browser.find_element(By.CSS_SELECTOR,"input#id_gender1").click()
        time.sleep(1)
        browser.find_element(By.ID,"customer_firstname").send_keys("isaghrib")
        time.sleep(1)
        browser.find_element(By.ID, "customer_lastname").send_keys("aziz")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[5]/input").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.ID, "days").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/select/option[29]").click()
        time.sleep(1)
        browser.find_element(By.ID, "months").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[2]/div/select/option[12]").click()
        time.sleep(1)
        browser.find_element(By.ID, "years").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[3]/div/select/option[26]").click()
        time.sleep(1)
        #Your Address
        browser.find_element(By.ID, "address1").send_keys("George Street")
        time.sleep(1)
        browser.find_element(By.ID, "city").send_keys("Jakarta Timur")
        time.sleep(1)
        browser.find_element(By.ID, "id_country").click()
        time.sleep(1)
        browser.find_element(By.ID, "id_state").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select/option[12]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "postcode").send_keys("13730")
        time.sleep(1)
        browser.find_element(By.NAME, "phone_mobile").send_keys("08888585")
        time.sleep(1)
        browser.find_element(By.NAME, "alias").clear()
        time.sleep(1)
        browser.find_element(By.NAME, "alias").send_keys("Jakarta Timur, 13730")
        time.sleep(1)
        browser.find_element(By.NAME, "submitAccount").click()
        time.sleep(1)
        
        text_atas = browser.find_element(By.ID, "center_column").text
        text_bawah = browser.find_element(By.CLASS_NAME, "info_account").text

        self.assertEqual(text_atas, 'My Account')
        self.assertIn("Welcome", text_bawah)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()