 #!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import qrcode
from bs4 import BeautifulSoup
import requests

from fake_useragent import UserAgent
import json
import cook_cookies
import time
import datetime
import pymysql
import pandas as pd


COOKIES=''

def Crash_data():
    global COOKIES
    cookies={}

    for line in open("cookies.txt","r"): 
        COOKIES=line
        cookies_list=COOKIES
    if not COOKIES:
        cookies_list=cook_cookies.gitlab_cookies()
        time.sleep(5)

    for line in cookies_list.split(';'):          
        name,value=line.strip().split('=',1)
        cookies[name]=value

    data={
    "queries":[
        {
            "refId":"A",
            "datasourceId":1,
            "rawSql":"select \n  dt as '日期',\n  app_id as '平台',\n  ver as '版本',\n  crash_cnt as '崩溃人数',\n  active_user_cnt as '日活',\n  crash_rate as '崩溃率'\nfrom ads_android_crash_rate_stat_day \nwhere app_id <> 'all'",
            "format":"table",
            "intervalMs":120000,
            "maxDataPoints":204
        }
    ],
    "range":{
        "from":"",
        "to":"",
        "raw":{
            "from":"now-6h",
            "to":"now"
        }
    },
    "from":"",
    "to":""
}
    headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.457'
 }

    try:
        response = requests.post('https://gf.caijiyouxi.com/api/ds/query', headers=headers,cookies=cookies,json=data,verify=False)

        htmlres=response.json()
        # print(htmlres['results']['A']['frames'][0]['data'])
        # sql_init(0,htmlres['results']['A']['frames'][0]['data'])
        return htmlres['results']['A']['frames'][0]['data']
    except:
        cookies_list=cook_cookies.gitlab_cookies()
        time.sleep(5)
        return Crash_data()

#写入数据库
#// date=1 #导入所有
#// data=0 #导入当天数据
def sql_init(date,data):
  #   conn = pymysql.connect(
  #   host='192.168.3.78',
  #   user='root',
  #   password='root123456',
  #   db='QA_Platfrom',
  #   port=3306
  # )
    today=str(datetime.date.today())
    print('today is'+today)
    print(data)
    
    if date==0:
        for indx_2,daily_data in enumerate(data['values'][0]):           
            if str(daily_data.strip()) == str(today.strip()):
                today=str(today.strip())
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
                print(today,version,crash_umb,dau,crash_rate)
                # cursor = conn.cursor() # 获取操作游标，也就是开始操作 
                # sql="INSERT INTO Chikii_crash_data(time,version,crash_umb,dau,crash_rate) VALUES(%s,%s,%s,%s,%s);"% (today,version,crash_umb,dau,crash_rate)     
                # cursor.executemany(sql)
                # conn.commit()
    # conn.close()
    # print('finished')


if __name__ == '__main__':
    # sql_init(0,0)
    sql_init(0,{'values': [['2021-09-08', '2021-09-08', '2021-09-09', '2021-09-09', '2021-09-13', '2021-09-13'], ['10018', '10018', '10018', '10018', '10018', '10018'], ['1.12.0-snapshot', 'all', '1.12.0-snapshot', 'all', '1.12.0-snapshot', 'all'], [6, 6, 3, 3, 3, 3], [None, 86422, None, 86416, None, 86416], [None, 0.0069, None, 0.0035, None, 0.0035]]})
