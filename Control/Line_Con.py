from Module import Browser
from Module import Browser as Browser_Module
import time
class Line:
    def __init__(self):
        self.Browser_fn = Browser_Module.Browser()
        self.Driver = self.Browser_fn.Init_Browser("../")

    def Start_Line(self):
        self.Driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")

        time.sleep(1)
        email_input = self.Driver.find_element_by_css_selector("#line_login_email")
        email_input.send_keys("johnplugintw@gmail.com")

        pwd_input = self.Driver.find_element_by_css_selector("#line_login_pwd")
        pwd_input.send_keys("Aa123456")

        login_btn = self.Driver.find_element_by_css_selector("#login_btn")
        login_btn.click()

        #判斷手機驗証碼是否通過了
        self.Check_Mobile_Captcha_Screen()
        print("驗証碼通過了哦")

    def Check_Mobile_Captcha_Screen(self):
        Stat = 1
        while Stat == 1:
           Captcha_Ele = self.Driver.find_element_by_css_selector("#login_area")
           if Captcha_Ele.is_displayed() == 0:
               Stat = 0

           time.sleep(0.1)


if __name__ == '__main__':
    obj = Line()
    obj.Start_Line()