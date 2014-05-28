from bok_choy.web_app_test import WebAppTest
from pages.Studio.homepage import HomePage
from pages.Studio.signup import SignUpPage
from pages.Studio.login import LoginPage
from pages.Studio.howstudioworks import HowStudioWorksPage
from pages.Studio.studiohelp import StudioHelpPage


class MyTest(WebAppTest):
    def setUp(self):
        super(MyTest, self).setUp()
        self.home_page = HomePage(self.browser)
        self.signup_page = SignUpPage(self.browser)
        self.login_page = LoginPage(self.browser)
        self.how_studio_works_page = HowStudioWorksPage(self.browser)
        self.studio_help_page = StudioHelpPage(self.browser)
        HomePage(self.browser).visit()

    # Verify that user can click edX Studio Image and is navigated to Home Page again
    def test_click_edx_image(self):
        self.home_page.click_edx_image()
        self.assertTrue(self.home_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Sign Up button and is navigated to the Sign up page
    def test_signup_button(self):
        self.home_page.click_signup_button()
        self.assertTrue(self.signup_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Login button and is navigated to the Login page
    def test_login_button(self):
        self.home_page.click_login_button()
        self.assertTrue(self.login_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click How Studio Works link and is navigated to How Studio Works page
    def test_how_studio_works_link(self):
        self.home_page.click_how_studio_works_link()
        self.assertTrue(self.how_studio_works_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Studio Help link and is navigated to Help page
    def test_studio_help_link(self):
        self.home_page.click_studio_help_link()
        self.assertTrue(self.studio_help_page.is_browser_on_page(), "Not on Correct Page or Link Broken")
