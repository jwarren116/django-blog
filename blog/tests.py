from django.test import LiveServerTestCase
from selenium import webdriver


class TestProfileView(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TestProfileView, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestProfileView, self).tearDown()

    def test_home(self):
        '''test that home page is available to visitor'''
        # self.selenium.get(self.live_server_url)
        assert self.selenium.find_element_by_id('projects')
        assert self.selenium.find_element_by_id('about')
        assert self.selenium.find_element_by_id('posts')

    def test_posts(self):
        '''test that post details and return links are available to visitor'''
        # self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_partial_link_text('Read more').click()
        assert self.selenium.find_element_by_class_name('detail-entry')
        self.selenium.find_element_by_partial_link_text('James Warren').click()
        assert self.selenium.find_element_by_id('summary')

    def test_link_scrolling(self):
        pass
