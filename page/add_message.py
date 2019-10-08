# 新建信息

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class Add_Message(BaseAction):

    # 信息接收者
    message_reciver = By.XPATH,"//*[@text='接收者']"

    # 信息内容
    message_text = By.XPATH,"//*[@text='键入信息']"

    # 发送按钮
    message_recive_btn = By.ID,"com.android.mms:id/send_button_sms"

    @allure.step(title="进行输入及发送操作")
    def input_message_reciver(self,text):
        allure.attach("输入接收者的电话号码", text, allure.attach_type.TEXT)
        self.input(self.message_reciver,text)

    def input_message_text(self,text):
        allure.attach("输入短信内容",text,allure.attach_type.TEXT)
        self.input(self.message_text,text)

    def click_message_recive_btn(self):
        self.click(self.message_recive_btn)
        allure.attach("发送成功截图",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)
