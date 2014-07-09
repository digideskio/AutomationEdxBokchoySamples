from bok_choy.page_object import PageObject
from pages.Studio import BASE_URL

class EdgeHelpPage(PageObject):
    """
    Edge Help Page
    """

    url = None

    def is_browser_on_page(self):
        return 'welcome - edx studio support' in self.browser.title.lower()