from seleniumbase import BaseCase
import time


file_path = "../data/111.png"

class UploadTest(BaseCase):

    def open_home_page(self):
        self.open("https://the-internet.herokuapp.com/upload")
        self.maximize_window()


    def test_upload_heroku(self):
        self.open_home_page()

        # get file path


        #upload file
        self.choose_file("#file-upload", file_path)
        time.sleep(3)

        self.click("#file-submit")

        self.assert_element('h3')
        self.assert_text("File Uploaded!", "h3")
        #self.assertEqual("h3", "File Uploaded!")


    def test_hidden_upload(self):
        self.open("https://practice.automationbro.com/cart/")
        self.maximize_window()

        # upload file to site
        self.choose_file("#upfile_1", file_path)
        # self.choose_file(".file_input_hidden", file_path)

        #add js code
        # remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        # self.add_js_code(remove_hidden_class)
        # time.sleep(3)
        # click submit button
        self.click(".file_input_submit")
        time.sleep(3)

        #assert file was uploaded
        uploaded_text = self.get_text("div>label.file_messageblock_fileheader_label")

        assert "uploaded successfully" in uploaded_text



