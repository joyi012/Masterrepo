from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
'#Enter User login credentials'
time.sleep(5)
driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(by=By.NAME, value="login-button").click()
time.sleep(5)
# Add multiple product in product in cart
driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-backpack").click()
driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bike-light").click()
time.sleep(5)
# Verify product inside cart
driver.find_element(by=By.ID, value="shopping_cart_container").click()
# Remove product from cart
time.sleep(5)
driver.find_element(by=By.ID,value="remove-sauce-labs-backpack").click()
# Processed to check out
time.sleep(5)
driver.find_element(by=By.ID, value="checkout").click()
time.sleep(5)
# Fill Address fields
driver.find_element(by=By.ID, value="first-name").send_keys("Rahul")
time.sleep(5)
driver.find_element(by=By.ID, value="last-name").send_keys("Kumar")
time.sleep(5)
driver.find_element(by=By.ID, value="postal-code").send_keys("455778")
time.sleep(5)
# Check price and product
driver.find_element(by=By.ID, value="continue").click()
time.sleep(10)
# Scrolldown page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# driver.send_keys(Keys.ARROW_DOWN)
time.sleep(10)
driver.find_element(by=By.NAME, value="finish").click()
driver.find_element(by=By.XPATH, value="//html").send_keys(Keys.CONTROL + Keys.HOME)
print("Thank you for Shopping")
time.sleep(10)
driver.close()
print("Code execute successfully ")
