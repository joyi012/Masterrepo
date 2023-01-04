from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")
driver.refresh()
source = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Prime Packs']")
action = ActionChains(driver)
# double click operation and perform
action.double_click(source).perform()
# to close the browser
driver.close()
