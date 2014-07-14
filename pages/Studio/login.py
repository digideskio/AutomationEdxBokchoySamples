from bok_choy.page_object import PageObject
from bok_choy.promise import EmptyPromise
from pages.Studio import BASE_URL
from pages.Studio.signup import SignUpPage
from pages.Studio.edgehelp import EdgeHelpPage
from pages.Studio.mycoursespage import MyCoursesPage

class LoginPage(PageObject):
    """
    Studio Login Page
    """

    url = BASE_URL + '/signin'

    def is_browser_on_page(self):
        return self.q(css='body.view-signin').present

    def click_dont_have_studio_account_link(self):
        # Click on Don't have a Studio Account? Sign up! link
        self.q(css='.content header a.action.action-signin').first.click()

    def click_our_support_center_link(self):
        # Click on Our Support Center link
        self.q(css='.bit p a').first.click()
        for handle in self.browser.window_handles:
            self.browser.switch_to_window(handle)
        EdgeHelpPage(self.browser).wait_for_page()

    def login(self, email, password):
        """
        Attempt to log in using `email` and `password`.
        """

        self.q(css='input#email').fill(email)
        self.q(css='input#password').fill(password)
        self.q(css='button#submit').first.click()

        # Ensure that we make it to another page

        #from nose.tools import set_trace; set_trace()
        EmptyPromise(
            lambda: "login" not in self.browser.current_url,
            "redirected from the login page"
        ).fulfill()

        #MyCoursesPage(self.browser).wait_for_page()