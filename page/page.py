# 页面统一入口
from page.add_message import Add_Message
from page.message_list import Message_List


class Page:

    def __init__(self,driver):
        self.driver = driver

    def del_add_all_message(self):
        return Message_List(self.driver)

    def add_message(self):
        return Add_Message(self.driver)
