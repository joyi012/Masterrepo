from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# for run un headless mode
chrome_options.add_argument("headless")
# disabled auto control message
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://www.scientecheasy.com/")
# page scroll down
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# For taking screenshot
driver.get_screenshot_as_file("screen.png")

