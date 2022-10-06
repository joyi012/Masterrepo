from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
'#disabled Automation control notification'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
"""
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
"""
'#Set driver path'
'# driver = webdriver.Chrome(executable_path="C:/Users/dell/Downloads/chromedriver_win32/chromedriver.exe", options=chrome_options)'
driver = webdriver.Chrome()
'#maximize window and hit on URL'
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
'#Enter User login credentials'
driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
driver.find_element(by=By.NAME, value="login-button").click()
time.sleep(5)
'# Add product in cart'
driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-backpack").click()
time.sleep(5)
'# Verify product inside cart'
driver.find_element(by=By.ID, value="shopping_cart_container").click()
time.sleep(5)
'# Processed to check out'
driver.find_element(by=By.ID, value="checkout").click()
time.sleep(5)
'# Fill Address fields'
driver.find_element(by=By.ID, value="first-name").send_keys("Rahul")
driver.find_element(by=By.ID, value="last-name").send_keys("Kumar")
driver.find_element(by=By.ID, value="postal-code").send_keys("455778")
time.sleep(5)
'# Check price and product'
driver.find_element(by=By.ID, value="continue").click()
time.sleep(10)
'# Scrolldown page'
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
'# driver.send_keys(Keys.ARROW_DOWN)'
time.sleep(10)
driver.find_element(by=By.NAME, value="finish").click()
print("Thank you for Shopping")
time.sleep(10)
driver.close()
print("Code execute successfully ")

