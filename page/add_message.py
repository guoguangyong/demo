# 新建信息
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Add_Message(BaseAction):

    # 信息接收者
    message_reciver = By.XPATH,"//*[@text='接收者']"

    # 信息内容
    message_text = By.XPATH,"//*[@text='键入信息']"

    # 发送按钮
    message_recive_btn = By.ID,"com.android.mms:id/send_button_sms"

    def input_message_reciver(self,text):
        self.input(self.message_reciver,text)

    def input_message_text(self,text):
        self.input(self.message_text,text)

    def click_message_recive_btn(self):
        self.click(self.message_recive_btn)