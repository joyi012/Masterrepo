from selenium import webdriver
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        '#web_driver = webdriver.Chrome(ChromeDriverManager().install())'
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
    if request.param == "firefox":
        '#web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())'
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()
        request.cls.driver = web_driver
        yield
        web_driver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("http://www.google.com")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
