from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# code to disabled chrom is being controlled
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)
'#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))'
driver = webdriver.Chrome(executable_path="C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe", options=chrome_options)
# driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://google.com')