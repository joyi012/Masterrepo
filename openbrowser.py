from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.saucedemo.com/")