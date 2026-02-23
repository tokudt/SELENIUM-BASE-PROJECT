from seleniumbase import BaseCase

class UITest(BaseCase):

    def test_desktop_ui(self):
        self.open("https://www.lazada.vn")
        self.set_window_size(1920, 1080)  # Desktop size
        self.sleep(2)


    def test_mobile_ui(self):
        self.open("https://www.lazada.vn")
        self.set_window_size(375, 667)  # iPhone 8 size
        self.sleep(2)