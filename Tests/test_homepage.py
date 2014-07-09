from bok_choy.web_app_test import WebAppTest
from pages.Studio.homepage import HomePage
from pages.Studio.signup import SignUpPage
from pages.Studio.login import LoginPage
from pages.Studio.howstudioworks import HowStudioWorksPage
from pages.Studio.studiohelp import StudioHelpPage
from pages.Studio.edxlivepage import EdxLivePage
from pages.Studio.termsofservice import TermsOfServicePage
from pages.Studio.privacypolicy import PrivacyPolicyPage

class MyTest(WebAppTest):
    def setUp(self):
        super(MyTest, self).setUp()
        self.home_page = HomePage(self.browser)
        self.signup_page = SignUpPage(self.browser)
        self.login_page = LoginPage(self.browser)
        self.how_studio_works_page = HowStudioWorksPage(self.browser)
        self.studio_help_page = StudioHelpPage(self.browser)
        self.edx_live_link = EdxLivePage(self.browser)
        self.edx_terms_page = TermsOfServicePage(self.browser)
        self.edx_privacy_policy_page = PrivacyPolicyPage(self.browser)
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

    # Verify that user can click Studio Help link and is navigated to Help page
    def test_studio_help_link(self):
        self.home_page.click_studio_help_link()
        self.assertTrue(self.studio_help_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Sign up & Start Making An Edx Course button and is navigated to the Sign up page
    def test_signup_start_making_edx_course_button(self):
        self.home_page.click_signup_and_start_making_button()
        self.assertTrue(self.signup_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Already have a Studio Account? Sign in link and is navigated to the Log in page
    def test_already_have_studio_account_link(self):
        self.home_page.click_already_have_studio_account_link()
        self.assertTrue(self.login_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click edx link and is navigated to edx live website
    def test_edx_live_link(self):
        self.home_page.click_edx_live_link()
        self.assertTrue(self.edx_live_link.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Terms of Service link and is navigated to Terms of Service page
    """
    On clicking Terms of service link it navigates to the page and displays Authentication box. This can be handled
    through AutoIt etc. Sticking to Selenium and Bok Choy, I am going to write 2 tests. One will check the url from the
    home page and verify that, the other will navigate to the page and will make sure the link is not broken
    """
    def test_terms_of_service_link(self):
        self.home_page.verify_terms_of_service_url()
        self.assertEquals(self.home_page.verify_terms_of_service_url(), "https://www.stage.edx.org/edx-terms-service")
        self.home_page.terms_of_service_page()
        self.assertTrue(self.edx_terms_page.is_browser_on_page(), "Not on Correct Page or Link Broken")

    # Verify that user can click Privacy Policy link and is navigated to Privacy Policy page
    """
    On clicking Privacy Policy link it navigates to the page and displays Authentication box. This can be handled
    through AutoIt etc. Sticking to Selenium and Bok Choy, I am going to write 2 tests. One will check the url from the
    home page and verify that, the other will navigate to the page and will make sure the link is not broken
    """
    def test_privacy_policy_link(self):
        self.home_page.verify_privacy_policy_url()
        self.assertEquals(self.home_page.verify_privacy_policy_url(), "https://www.stage.edx.org/edx-privacy-policy")
        self.home_page.privacy_policy_page()
        self.assertTrue(self.edx_privacy_policy_page.is_browser_on_page(), "Not on Correct Page or Link Broken")