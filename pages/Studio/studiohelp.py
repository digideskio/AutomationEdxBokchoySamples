from bok_choy.page_object import PageObject
from pages.Studio import BASE_URL

class StudioHelpPage(PageObject):
    """
    Studio Help page
    """
    url = None

    def is_browser_on_page(self):
        return 'getting started with studio' in self.browser.title.lower()
