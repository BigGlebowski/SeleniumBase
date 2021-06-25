from seleniumbase import BaseCase
import time
from page_object.home_page import HomePage

class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        print("Its start of the every test")
        self.open("https://practice.automationbro.com/")
        self.maximize_window()
        #self.login()


    def tearDown(self):
        #self.logout()
        super().tearDown()
        print("its the end of every test")
        




    def test_home_page(self):
        #self.open_home_page()

        #assert page title
        self.assert_title_of_page("Practice E-Commerce Site – Automation Bro")

        #assert logo
        self.assert_element("img[class='custom-logo']")

        # click on the get started button and assert the link
        self.click('#get-started')
        self.assertEqual("https://practice.automationbro.com/#get-started", self.get_current_url())

        #get the text of the header and assert value
        self.assert_text("Zakra Invites You To Build Your Next Site", "h3[class='elementor-heading-title elementor-size-default']")

        # scroll to the bottom and assert copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", "div[class='tg-site-footer-section-1']>p")


    def test_menu_links(self):
        #self.open_home_page()

        # find menu link elements
        menu_links = self.find_elements(".//nav[@id='site-navigation']//*[starts-with(@id, 'menu-item')]")
        links_names = []
        for menu_link in menu_links:
            links_names.append(menu_link.text)

        #print(links_names)
        correct_menu_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']
        self.assertEqual(correct_menu_links, links_names)

    def test_contact_page(self):
        #self.open_home_page()
        self.go_to_link('Contact')
        self.fill_in_contact_info()
        self.assertEqual(self.contact_message_success(), "Thanks for contacting us! We will be in touch with you shortly")





