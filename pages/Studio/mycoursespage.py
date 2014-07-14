from bok_choy.page_object import PageObject
from pages.Studio import BASE_URL

class MyCoursesPage(PageObject):
    """
    My Courses Page after logging in
    """

    url = None

    def is_browser_on_page(self):
        return 'my courses | edx studio' in self.browser.title.lower()