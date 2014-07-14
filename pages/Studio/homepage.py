from bok_choy.page_object import PageObject
from pages.Studio import BASE_URL
from pages.Studio.signup import SignUpPage
from pages.Studio.login import LoginPage
from pages.Studio.studiohelp import StudioHelpPage
from pages.Studio.edxlivepage import EdxLivePage
from pages.Studio.termsofservice import TermsOfServicePage
from pages.Studio.privacypolicy import PrivacyPolicyPage

class HomePage(PageObject):
    """
    Studio Home Page
    """

    url = BASE_URL

    def is_browser_on_page(self):
        return 'welcome' in self.browser.title.lower()

    def click_edx_image(self):
        # Clicks on the EDX image
        self.q(css='img[alt=\"edX Studio\"]').first.click()
        HomePage(self.browser).wait_for_page()

    def click_signup_button(self):
        # Clicks on Sign up button
        self.q(css='.action-signup').first.click()
        SignUpPage(self.browser).wait_for_page()

    def click_login_button(self):
        # Clicks on Sign in button
        self.q(css='.action-signin').first.click()
        LoginPage(self.browser).wait_for_page()

    def click_studio_help_link(self):
        # Clicks on Studio Help link
        self.q(css='.nav-not-signedin-help > a').first.click()
        self.browser.switch_to_window(self.browser.window_handles[-1])
        StudioHelpPage(self.browser).wait_for_page()

    def click_signup_and_start_making_button(self):
        # Clicks on Sign up & Start Making An Edx Course button
        self.q(css='.action-primary').first.click()
        SignUpPage(self.browser).wait_for_page()

    def click_already_have_studio_account_link(self):
        # Clicks on Already have a Studio Account? Sign in
        self.q(css='.action-secondary').first.click()
        LoginPage(self.browser).wait_for_page()

    def click_edx_live_link(self):
        # Clicks on edx Live link
        self.q(css='footer.primary div.colophon p a').first.click()
        self.browser.switch_to_window(self.browser.window_handles[-1])
        EdxLivePage(self.browser).wait_for_page()

    def verify_terms_of_service_url(self):
        # Verify terms and service url
        return self.q(css='li.nav-item.nav-peripheral-tos a').attrs('href')[0]

    def terms_of_service_page(self):
        # Terms of Service page is displaying
        TermsOfServicePage(self.browser).visit().wait_for_page()

    def verify_privacy_policy_url(self):
        # Verify privacy policy url
        return self.q(css='li.nav-item.nav-peripheral-pp a').attrs('href')[0]

    def privacy_policy_page(self):
        # Privacy Policy page is displaying
        PrivacyPolicyPage(self.browser).visit().wait_for_page()