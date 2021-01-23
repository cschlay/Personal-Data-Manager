from utils.testing import LiveTestCase


class MySeleniumTests(LiveTestCase):

    def test_login(self):
        self.browser.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('secret')
        self.browser.find_element_by_id("login-button")
