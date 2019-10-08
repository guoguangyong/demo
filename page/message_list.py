import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Message_List(BaseAction):
    # 点击。。。（更多）选项
    more_btn = By.CLASS_NAME,"android.widget.ImageButton"

    count = random.randint(1,2)

    # 点击设置
    setting = By.XPATH,"//*[@text='设置']"

    # 返回按钮
    back_btn = By.ID,"android:id/up"

    # 选择删除所有信息
    delete_all_message_btn = By.XPATH,"//*[@text='删除所有会话']"

    # 确认删除
    sure_del_all_message = By.XPATH,"//*[@text='删除']"

    # 选择添加信息
    add_message_btn = By.ID,"com.android.mms:id/action_compose_new"

    # 点击更多操作
    def click_more_btn(self):
        self.click(self.more_btn)
        if self.count != 1:
            self.click(self.delete_all_message_btn)
            self.click(self.sure_del_all_message)
            self.click(self.add_message_btn)

        else:
            self.click(self.setting)
            self.click(self.back_btn)
            self.click(self.add_message_btn)