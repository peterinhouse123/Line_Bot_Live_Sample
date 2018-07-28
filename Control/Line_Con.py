from Module import Browser
from Module import Browser as Browser_Module

from selenium.webdriver.common.keys import Keys
import time
import json
class Line:
    def __init__(self,parse_dir="../"):
        self.Browser_fn = Browser_Module.Browser()
        self.parse_dir = parse_dir
        self.Driver = None
        self.Friend_List = []

        self.WS_Login_Success_Callback = None


    def Start_Line(self,client=None,account_pack=None):
        # account_pack = json.loads(account_pack)
        account = account_pack['account']
        password = account_pack['password']

        self.Driver = self.Browser_fn.Init_Browser(self.parse_dir)
        self.Driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")

        time.sleep(1)
        email_input = self.Driver.find_element_by_css_selector("#line_login_email")
        email_input.send_keys(account)

        pwd_input = self.Driver.find_element_by_css_selector("#line_login_pwd")
        pwd_input.send_keys(password)

        login_btn = self.Driver.find_element_by_css_selector("#login_btn")
        login_btn.click()

        #判斷手機驗証碼是否通過了
        self.Check_Mobile_Captcha_Screen()
        print("驗証碼通過了哦")
        time.sleep(3)
        if self.WS_Login_Success_Callback != None:
            self.WS_Login_Success_Callback(client)

        self.Get_Friend_List()
        self.Send_Mesg_To_Friend(mid="u46710a7f314832fce484bf63bd0eaf4f",msg_body="hello")


    def Send_Mesg_To_Friend(self,mid,msg_body):
        self.Click_Firend_Tab()
        Friend_ele = self.Driver.find_element_by_xpath('//li[@data-mid="'+format(mid)+'"]')
        Friend_ele.click()

        Chat_Input = self.Driver.find_element_by_css_selector("#_chat_room_input")
        Chat_Input.send_keys(msg_body)
        Chat_Input.send_keys(Keys.ENTER)



    def Click_Firend_Tab(self):
        Friends_btn = self.Driver.find_element_by_xpath('//li[@data-type="friends_list"]')
        Friends_btn.click()
        # time.sleep(1)

    def Get_Friend_List(self,no_ele=0):

        Friend_list = self.Driver.find_elements_by_css_selector(".mdMN02Li")

        end = []

        for ele in Friend_list:
            name = ele.find_element_by_css_selector(".mdCMN04Ttl").text
            pack = {}
            if no_ele == 0:
                pack['ele'] = ele
            pack['name'] = name
            pack['mid'] = ele.get_attribute("data-mid")
            end.append(pack)
        self.Friend_List = end

        return end




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