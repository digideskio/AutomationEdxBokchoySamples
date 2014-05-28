__author__ = 'mac'
from bok_choy.page_object import PageObject
from . import BASE_URL


class HomePage(PageObject):
    """
    Edx Home Page
    """
    # This URL will be the one that you want to run tests on
    url = BASE_URL

    # Checks if the browser is on the right page by login button and register now button
    def is_browser_on_page(self):
        return self.q(
            css='#block-system-user-menu > ul > li.first.leaf.menu-depth-1.menu-item-8144 > a').present and self.q(
            css='#primary-menu-bar > nav > ul > li.menu-7492.last > a').present