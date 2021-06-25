from page_object.home_page import HomePage
from page_object.shop_page import ShopPage
from seleniumbase import BaseCase



class Application():

    def __init__(self):
        self.home = HomePage()
        self.shop = ShopPage()



class BaseTestClass(BaseCase):
    app = Application()

    def setUp(self):
        super(BaseTestClass, self).setUp()
        print("Its start of the every test")
        self.open("https://practice.automationbro.com/")
        self.maximize_window()
        # self.login()

    def tearDown(self):
        # self.logout()
        super(BaseTestClass, self).tearDown()
        print("its the end of every test")

