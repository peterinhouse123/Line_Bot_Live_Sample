#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
from websocket_server import WebsocketServer
import time
import logging
import os
import subprocess
import json

#The UI Base on WS and HTML

class WUI():
    def __init__(self,theme_path,
                 browser_path,
                 log_lv=logging.DEBUG,
                 exit_time=10,
                 host='0.0.0.0',
                 port=6677):

        logging.basicConfig(level=log_lv)

        self.port = port
        self.CREATE_NO_WINDOW = 0x08000000
        self.exit_time = exit_time
        self.theme_path = theme_path
        self.browser_path = browser_path

        self.User_List = []

        self.host = host

        self.init_stat = 0

        self.Recv_Message_Hook = list()
        self.Join_Hook = list()
        self.Leave_Hook = list()

        self.init_ws()

    def init_ws(self):
        self.ws = WebsocketServer(self.port, host=self.host)
        self.ws.set_fn_message_received(self.message_received)
        self.ws.set_fn_client_left(self.user_leave)
        self.ws.set_fn_new_client(self.user_join)

        t = Thread(target=self.Exit_Check)
        t.start()

    def Send_Order(self,client,order,detail):
        temp = dict()
        temp['order'] = order
        temp['detail'] = detail
        temp = json.dumps(temp)
        self.ws.send_message(client,temp)
    def Broadcast(self,order,detail):
        temp = dict()
        temp['order'] = order
        temp['detail'] = detail
        temp = json.dumps(temp)
        self.ws.send_message_to_all(temp)

    def Add_Recv_Msg_Hook(self,msg_txt,callback,send_msg_to_fn=1):
        self.Add_WS_Hook('rec',msg_txt,callback,send_msg_to_fn)
    def Add_Join_Hook(self,callback='',msg_txt='',send_msg_to_fn=1):
        self.Add_WS_Hook('join',msg_txt,callback,send_msg_to_fn)
    def Add_Leave_Hook(self,msg_txt,callback,send_msg_to_fn=1):
        self.Add_WS_Hook('leave',msg_txt,callback,send_msg_to_fn)

    def Add_WS_Hook(self,hook_type,msg_txt,callback,send_msg_to_fn=1):
        try:
            mb = dict()
            mb['txt'] = msg_txt
            mb['callback'] = callback
            mb['send_msg_to_fn'] = send_msg_to_fn

            if hook_type == 'rec':
                self.Recv_Message_Hook.append(mb)
            if hook_type == 'join':
                self.Join_Hook.append(mb)
            if hook_type == 'leave':
                self.Leave_Hook.append(mb)
        except:
            print("Add_Hook_Error:"+format(msg_txt))

    def Run_Hook(self,hook_type,client,message):

        hook_list = list()
        if hook_type == 'rec':
            hook_list = self.Recv_Message_Hook
        if hook_type == 'join':
            hook_list = self.Join_Hook
        if hook_type == 'leave':
            hook_list = self.Leave_Hook

        for mb in hook_list:
            try:
                if hook_type == 'rec':
                    if mb['send_msg_to_fn'] == 1:
                        try:
                            msg_o = json.loads(message)
                            order = msg_o['order']
                            detail = msg_o['detail']
                            if order == mb['txt']:
                                mb['callback'](client, detail)
                        except Exception as e :
                            print(e)
                            logging.info("Message:"+format(message)+"JSON_Decode_Error")
                    else:
                        if message == mb['txt']:
                            mb['callback']()
                else:

                    if mb['send_msg_to_fn'] == 1:
                        mb['callback'](client)
                    else:
                        mb['callback']()
            except:
                print('Hook_Error:'+mb)


    def message_received(self, client, server, message):
        logging.debug("WS_Rec_Msg:"+format(message))
        self.Run_Hook(hook_type='rec',client=client,message=message)



    def user_leave(self,client,server):

        uid = client['id']
        del self.User_List[self.User_List.index(uid)]

        self.Run_Hook(hook_type='leave',client=client, message='')

    def user_join(self,client,server):
        logging.debug("User_Join:" + format(client))
        uid = client['id']
        self.User_List.append(uid)

        self.Run_Hook(hook_type='join',client=client, message=client)

    def Start_WS(self,start_browser=1):
        logging.info("Start_WS_Server:" + self.host+":"+format(self.port))
        t = Thread(target=self.ws.run_forever)
        t.start()
        if start_browser == 1:
            self.Start_Chrome()

    def Start_Chrome(self):
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        Self_chrome_path = self.browser_path

        if os.path.isfile(chrome_path) == True:
            order = [chrome_path, '%s', self.theme_path]
            subprocess.Popen(order)
        else:
            order = [Self_chrome_path, '%s', self.theme_path]
            subprocess.Popen(order)

    def Quit(self):
        pid = os.getpid()
        subprocess.Popen(args=['taskkill','/f','/PID',str(pid)],creationflags=self.CREATE_NO_WINDOW)

    def Exit_Check(self):
        zero_time = time.time()
        while 1:
            if len(self.User_List) != 0:
                zero_time = time.time()

            if zero_time != 0:
                af_time = time.time() - zero_time

                if af_time > self.exit_time:
                    self.Quit()

            time.sleep(0.3)
if __name__ == "__main__":
    obj = WUI('theme','tool')
