import time

from base.base_driver import init_driver
from page.page import Page


class Test_Message_Option:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_add_del_message(self):
        self.page.del_add_all_message().click_more_btn()
        self.page.add_message().input_message_reciver(11111111111)
        self.page.add_message().input_message_text("您好！")
        self.page.add_message().click_message_recive_btn()