from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class LiveTestCase(StaticLiveServerTestCase):
    # Uses firefox.
    # https://docs.djangoproject.com/en/3.1/topics/testing/tools/#liveservertestcase

    @classmethod
    def setUpClass(cls):
        """
        Setups Selenium with Firefox.
        """
        super().setUpClass()
        cls.browser = WebDriver()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

