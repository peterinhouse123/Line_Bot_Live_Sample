import os
import time
from Module import WS_UI
from Control import Line_Con


class Main:
    def __init__(self):
        self.WS_UI = WS_UI.WUI("","",exit_time=99999)
        self.Line = Line_Con.Line("")
        self.Init_WS_fn()
        self.Weboscket_Server()



    def Init_WS_fn(self):

        self.WS_UI.Add_Recv_Msg_Hook("login", self.Line.Start_Line)
        self.WS_UI.Add_Recv_Msg_Hook("renew_friend_list", self.WS_Renew_Friend_List)



        self.Line.WS_Login_Success_Callback = self.Send_Login_Success_Message

    def Send_Login_Success_Message(self,client):
        self.WS_UI.Send_Order(client,"login_success","")

    def WS_Renew_Friend_List(self,client,msg):
        Friend_List = self.Line.Get_Friend_List(no_ele=1)
        self.WS_UI.Send_Order(client,"Friend_List",Friend_List)


    def Weboscket_Server(self):
        self.WS_UI.Start_WS(start_browser=0)

    def Start(self):
        pass
        # self.Driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")






if __name__ == '__main__':
    obj = Main()
    obj.Start()