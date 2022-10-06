from selenium import webdriver
ddriver = webdriver.Chrome(executable_path="C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")