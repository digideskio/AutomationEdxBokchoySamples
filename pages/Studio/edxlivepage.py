from bok_choy.page_object import PageObject

class EdxLivePage(PageObject):
    """
    EDX Live Website
    """
    url = None

    def is_browser_on_page(self):
        return 'edx - online courses and classes from the' in self.browser.title.lower()
