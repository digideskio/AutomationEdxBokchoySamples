from bok_choy.page_object import PageObject
from pages.Studio import BASE_URL
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.Studio.signup import SignUpPage
from pages.Studio.login import LoginPage
from pages.Studio.howstudioworks import HowStudioWorksPage
from pages.Studio.studiohelp import StudioHelpPage


class HomePage(PageObject):
    """
    Studio Home Page
    """

    url = BASE_URL

    def is_browser_on_page(self):
        # Check the presence of Sign up and start making an edx course button to see if it's the correct page

        #from nose.tools import set_trace; set_trace()
        #return 'welcome to edx studio' == self.q(css="section.content header h1").text[0].strip().lower()

        return 'welcome' in self.browser.title.lower()

    def click_edx_image(self):
        # Clicks on the EDX image
        self.q(css='img[alt=\"edX Studio\"]').first.click()
        #return HomePage(self.browser).wait_for_page()

    def click_signup_button(self):
        # Clicks on Sign up button
        self.q(css='.action-signup').first.click()
        return SignUpPage(self.browser).wait_for_page()

    def click_login_button(self):
        # Clicks on Sign in button
        self.q(css='.action-signin').first.click()
        return LoginPage(self.browser).wait_for_page()

    def click_how_studio_works_link(self):
        # Clicks on How Studio Works link
        self.q(css='.nav-not-signedin-hiw').first.click()
        return HowStudioWorksPage(self.browser).wait_for_page()

    def click_studio_help_link(self):
        # Clicks on Studio Help link
        self.q(css='.nav-not-signedin-help > a').first.click()
        for handle in self.browser.window_handles:
            self.browser.switch_to_window(handle)
        return StudioHelpPage(self.browser).wait_for_page()