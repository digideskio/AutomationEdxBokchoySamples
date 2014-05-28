from bok_choy.page_object import PageObject
from pages.Studio import BASE_URL

class HowStudioWorksPage(PageObject):
    """
    How Studio Works (Help) page
    """
    url = None

    def is_browser_on_page(self):
        return self.q(css='body.section-dashboard').present