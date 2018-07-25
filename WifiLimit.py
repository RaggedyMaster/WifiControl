# -*- coding: utf-8 -*-

import json
import requests
import time
import re
import sys
import urllib
import getpass
from prettytable import PrettyTable
from imp import reload
import base64
import socket
import random

host = '192.168.1.1'
password = base64.b64encode("admin:"+"a1b2c3d4")#Please change your password at here
cookie = {"Authorization":"Basic " + password}
def CloseControl(sbit):
    url_password = "http://192.168.1.1/userRpm/QoSCfgRpm.htm?QoSCtrl="+str(sbit)+"&userWanType=0&down_bandWidth=102400&up_bandWidth=102400&Save=%B1%A3%20%B4%E6"
    headers = { 
        'Host': host,
        'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)',  
        'Referer' : 'http://'+ host +'/userRpm/QoSCfgRpm.htm',
        }
    response = requests.get(url = url_password,headers = headers,cookies = cookie)

def FuckIp(ControlId,ip,speed,):
    if(ip[1]=="#"):
        url_password = "http://192.168.1.1/userRpm/QoSCfgRpm.htm?enable=true&start_ip_addr="+ip[0]+"&end_ip_addr="+"&min_up_band_width=0&max_up_band_width=0&min_down_band_width=0&max_down_band_width="+speed+"&Save=%B1%A3+%B4%E6&curEditId="+ControlId+"&Page=1"
    else:       
        url_password = "http://192.168.1.1/userRpm/QoSCfgRpm.htm?enable=true&start_ip_addr="+ip[0]+"&end_ip_addr="+ip[1]+"&min_up_band_width=0&max_up_band_width=0&min_down_band_width=0&max_down_band_width="+speed+"&Save=%B1%A3+%B4%E6&curEditId="+ControlId+"&Page=1"
    headers = { 
        'Host': host,
        'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)',  
        'Referer' : 'http://'+ host +'/userRpm/QoSCfgRpm.htm',
        }
    response = requests.get(url = url_password,headers = headers,cookies = cookie)
    
if __name__ == '__main__':
    ControlIdAll=["101","65637","131173","196709","262245","327781","393317"]
    url_login = 'http://' + host
    response = requests.get(url = url_login,cookies = cookie)
    serverResult = ''.join(response.text.split())
    ifSuccess = serverResult.split('userRpm')
    if len(ifSuccess) < 2:
        loginStatus = re.findall(r'varhttpAutErrorArray=newArray\((.+?),"http',serverResult)
        print('Login Failed. Status is ' + loginStatus[0])
    else:
        print('Login Success.')

    addrs = socket.getaddrinfo(socket.gethostname(),None)
    for item in addrs:
        if(item[4][0][0:10]=='192.168.1.'):
            MyIp=item[4][0]

    
    
    if(MyIp=='192.168.1.1'):
        list1 = range(250)
        randomlist=random.sample(list1, 1)
        randomlist.sort()
        IpSum=["192.168.1.2"]
        for i in randomlist:
            IpSum.append("192.168.1."+str(i+2))
            IpSum.append("192.168.1."+str(i+3))
            IpNum.append(2)
        IpSum.append("192.168.1.255")
    elif(MyIp=='192.168.1.255'):
        list1 = range(249)
        randomlist=random.sample(list1, 1)
        randomlist.sort()
        IpSum=["192.168.1.1"]
        for i in randomlist:
            IpSum.append("192.168.1."+str(i+3))
            IpSum.append("192.168.1."+str(i+4))
        IpSum.append("192.168.1.254")
    elif(MyIp=='192.168.1.2'):
        IpSum=["192.168.1.2","#","192.168.1.3","192.168.1.255"]
    elif(MyIp=='192.168.1.254'):
        IpSum=["192.168.1.1","192.168.1.253","192.168.1.255","#"]
    else:
        IpSum=["192.168.1.1"]
        num=int(MyIp[10:len(MyIp)])
        IpSum.append("192.168.1."+str(num-1))
        IpSum.append("192.168.1."+str(num+1))
        IpSum.append("192.168.1.255")
    
 
    IpInit=["192.168.1.1","#","192.168.1.2","#"]
    for i in range(2):
        ip=IpInit[2*i:2*i+2]
        speed=random.randint(300,500)
        FuckIp(ControlIdAll[i],ip,str(speed))
        time.sleep(1)
    time.sleep(1)
    for i in range(2):
        ip=IpSum[2*i:2*i+2]
        speed=random.randint(300,500)
        FuckIp(ControlIdAll[i],ip,str(speed))
        time.sleep(1)
    for i in range(2):
        ip=IpSum[2*i:2*i+2]
        speed=random.randint(300,500)
        FuckIp(ControlIdAll[i],ip,str(speed))
        time.sleep(1)
    print("Done!")

    
