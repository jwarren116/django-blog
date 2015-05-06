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
    screen_shot = factory.django.ImageField(color='blue')
    description = 'Some details'
    link = 'http://www.someproject.co/'
    display = True


class TestHomeView(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.post = PostFactory.create()
        self.project = ProjectFactory.create()
        super(TestHomeView, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestHomeView, self).tearDown()

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

    def test_projects(self):
        '''test that projects are displayed on index page for visitor'''
        self.selenium.get(self.live_server_url)
        assert self.selenium.find_element_by_class_name('img-thumbnail')
        self.assertIn('Some Project', self.selenium.page_source)

    def test_invalid_post_id(self):
        '''test that a propper 404 is returned when asking for an invalid post'''
        invalid_url = self.live_server_url + "/876"
        self.selenium.get(invalid_url)
        self.assertIn('Page not found', self.selenium.page_source)
