from django.test import LiveServerTestCase
from blog.models import BlogPost, Project
from selenium import webdriver
import factory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = 'Post'
    post = 'This is a new post'
    display = True


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = 'Some Project'
    description = 'Some details'
    link = 'http://www.jwarren.co/'
    display = True


class TestProfileView(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.post = PostFactory.create()
        super(TestProfileView, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestProfileView, self).tearDown()

    def test_home(self):
        '''test that home page is available to visitor'''
        self.selenium.get(self.live_server_url)
        assert self.selenium.find_element_by_id('projects')
        assert self.selenium.find_element_by_id('about')
        assert self.selenium.find_element_by_id('posts')

    def test_posts(self):
        '''test that post details and return links are available to visitor'''
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_partial_link_text('Read more').click()
        assert self.selenium.find_element_by_class_name('detail-entry')
        self.selenium.find_element_by_partial_link_text('James Warren').click()
        assert self.selenium.find_element_by_id('summary')
