# -*- coding: utf-8 -*-


import requests

import os 
import base64
import hashlib
import chikii_crashumb
import datetime

#处理爬虫数据 
def getCrash_data(data):
    daily_list={}
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday
    for indx_2,daily_data in enumerate(data['values'][0]):           
        if str(daily_data) == str(yesterday):
            yesterday=str(yesterday)
            for indx_3,daily_data1 in enumerate(data['values'][2]): 
                if indx_3 is indx_2:
                    version=str(daily_data1)
            for indx_4,daily_data2 in enumerate(data['values'][3]): 
                if indx_4 is indx_2:
                    crash_umb=str(daily_data2)
            for indx_5,daily_data3 in enumerate(data['values'][4]): 
                if indx_5 is indx_3:
                    dau=str(daily_data3)
            for indx_6,daily_data4 in enumerate(data['values'][5]): 
                if indx_6 is indx_2:
                    crash_rate=str(daily_data4)
                    if not crash_rate:
                        crash_rate=str(0)  
            daily_list[version]=[crash_umb,dau,crash_rate]
    print(daily_list)
    return daily_list

def wxRobot_msg(webhook_url):
    #机器人消息配置
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday

    data1=chikii_crashumb.Crash_data()
    data2=getCrash_data(data1)




    msg1='Chikii 昨日<font color=\"comment\">'+str(yesterday)+'</font>崩溃率：\n>'
    msg2=''

    for k,v in data2.items():
        if v[2]:
            msg2=msg2+'版本号:<font color=\"info\">'+str(k)+'</font>>>>崩溃率:<font color="warning">'+str(v[2])+'%'+'</font>\n'
    msg_data=msg1+msg2
    msg_all={
    "msgtype": "markdown",
    "markdown": {
        "content": msg_data
    }
}
    
    
    headers = {
        'Content-Type': 'application/json'}
    url= webhook_url
    response = requests.request("POST", url, headers=headers, json=msg_all,verify=False)


if __name__ == '__main__':
    
    wxRobot_msg('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f9bb22d2-15fe-4d01-b562-ebbeeeeeec1e')

            

