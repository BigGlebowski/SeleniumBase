import time
from seleniumbase import BaseCase

class HomePage(BaseCase):

    def logout(self):
        self.scroll_to_top()
        time.sleep(3)
        self.click("//*[@id='primary-menu']//a[text() = 'My account']")
        self.click("//a[contains(text(), 'Logout')]")
        self.assert_element_present("//h2[text()='Login']")

    def login(self):
        # login
        self.click("//*[@id='primary-menu']//a[text() = 'My account']")
        # try to login
        self.send_keys("//h2[text()='Login']/..//input[@id='username']", "qwe@gmail.com")
        self.send_keys("//h2[text()='Login']/..//input[@id='password']", "QweRT1231!@#")
        self.click("//h2[text()='Login']/..//*[@type='submit']")

        # if error is appeared, then register
        if len(self.find_elements("ul.woocommerce-error")) > 0:
            # register
            self.send_keys("//h2[text()='Register']/..//input[@id='reg_username']", "qweqwe")
            self.send_keys("//h2[text()='Register']/..//input[@id='reg_email']", "qwe@gmail.com")
            self.send_keys("//h2[text()='Register']/..//input[@id='reg_password']", "QweRT1231!@#")
            self.click("//h2[text()='Register']/..//*[@type='submit']")
            # QweRT1231!@#
        self.click(".custom-logo-link")


    def go_to_link(self, link_name):
        self.click(f"//ul[@id='primary-menu']//a[contains(text(), '{link_name}')]")


    def fill_in_contact_info(self):
        self.type("//span[text()='Name']/../../input", "test name")
        self.type("//span[text()='Email']/../../input", "test@mail.org")
        self.type("//span[text()='Phone']/../../input", "+3809999999999")
        self.type("//span[text()='Message']/../../textarea", "Hey, thank you for your video courses!:)")
        self.click("button[type='submit']")

    def contact_message_success(self):
        return self.get_text(".everest-forms")

    def assert_title_of_page(self,title):
        self.assert_title(title)