from bok_choy.web_app_test import WebAppTest
from pages.Studio.signup import SignUpPage
from pages.Studio.edgehelp import EdgeHelpPage
from pages.Studio.login import LoginPage
from pages.Studio.mycoursespage import MyCoursesPage

class MyTest(WebAppTest):
    def setUp(self):
        super(MyTest, self).setUp()
        self.login_page = LoginPage(self.browser)
        self.signup_page = SignUpPage(self.browser)
        self.edge_help_page = EdgeHelpPage(self.browser)
        self.mycourses_page = MyCoursesPage(self.browser)

        LoginPage(self.browser).visit()

    # Verify that user can click Don't have a Studio Account? Sign up! link and is navigated to Sign Up page
    def test_dont_have_studio_account_link(self):
        self.login_page.click_dont_have_studio_account_link()
        self.assertTrue(self.signup_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click our support center link and is navigated to Edge Help page
    def test_our_support_center_link(self):
        self.login_page.click_our_support_center_link()
        self.assertTrue(self.edge_help_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can login successfully
    def test_successful_login(self):
        self.login_page.login('raees.chachar@arbisoft.com', 'edx')
        self.assertTrue(self.mycourses_page.is_browser_on_page())
