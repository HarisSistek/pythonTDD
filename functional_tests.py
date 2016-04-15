"""Small function test."""

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage.
        self.browser.get('http://localhost:8000')


        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into the box

        # When she hits enter, the page updates, and now the page lists
        # 1: Buy peacock feathers as an item in a to-do lists

        # there is still a text box inviting her to add another item
        # she enters "Use peacock feathers to make a fly"

        # the page updates again and now shows both itmes on her lists

        # edit wonders whether the site will remember her list. then
        # she sees that the site has generated a unique URL for her
        # there is some extra text to explain the URL

        # she visits the URL and her to-do list is still there

        # satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
