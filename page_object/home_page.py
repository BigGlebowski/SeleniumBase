import time
#from seleniumbase import BaseCase

class HomePage():

    def logout(self, sb):
        sb.scroll_to_top()
        time.sleep(3)
        sb.click("//*[@id='primary-menu']//a[text() = 'My account']")
        sb.click("//a[contains(text(), 'Logout')]")
        sb.assert_element_present("//h2[text()='Login']")

    def login(self, sb):
        # login
        sb.click("//*[@id='primary-menu']//a[text() = 'My account']")
        # try to login
        sb.send_keys("//h2[text()='Login']/..//input[@id='username']", "qwe@gmail.com")
        sb.send_keys("//h2[text()='Login']/..//input[@id='password']", "QweRT1231!@#")
        sb.click("//h2[text()='Login']/..//*[@type='submit']")

        # if error is appeared, then register
        if len(sb.find_elements("ul.woocommerce-error")) > 0:
            # register
            sb.send_keys("//h2[text()='Register']/..//input[@id='reg_username']", "qweqwe")
            sb.send_keys("//h2[text()='Register']/..//input[@id='reg_email']", "qwe@gmail.com")
            sb.send_keys("//h2[text()='Register']/..//input[@id='reg_password']", "QweRT1231!@#")
            sb.click("//h2[text()='Register']/..//*[@type='submit']")
            # QweRT1231!@#
        sb.click(".custom-logo-link")


    def go_to_link(self, sb, link_name):
        sb.click(f"//ul[@id='primary-menu']//a[contains(text(), '{link_name}')]")


    def fill_in_contact_info(self, sb):
        sb.type("//span[text()='Name']/../../input", "test name")
        sb.type("//span[text()='Email']/../../input", "test@mail.org")
        sb.type("//span[text()='Phone']/../../input", "+3809999999999")
        sb.type("//span[text()='Message']/../../textarea", "Hey, thank you for your video courses!:)")
        sb.click("button[type='submit']")

    def contact_message_success(self, sb):
        return sb.get_text(".everest-forms")

    def assert_title_of_page(self, sb, title):
        sb.assert_title(title)