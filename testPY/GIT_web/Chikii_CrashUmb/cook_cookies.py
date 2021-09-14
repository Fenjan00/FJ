# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
import time
 


def gitlab_cookies():
    sel = selenium.webdriver.Chrome()
    loginurl = 'https://gf.caijiyouxi.com/login'
        #open the login in page
    sel.get(loginurl)
    time.sleep(3)

    sel.find_element_by_xpath("//*[@id='reactRoot']/div/div[2]/div[3]/div/div[2]/div/div/div[2]/a").click()
     

    try:
        sel.find_element_by_xpath("//*[@id='user_login']").send_keys('fengjian@caiji668.com')
        sel.find_element_by_xpath("//*[@id='user_password']").send_keys('Fenj851507786')
        time.sleep(3)
        sel.find_element_by_xpath("//*[@id='new_user']/div[5]/input").click()
    except:
    	print('登录gitlab失败')
    	return False

    #get the session cookie
    cookie = [item["name"] + "=" + item["value"] for item in sel.get_cookies()]
    #print cookie
     
    cookiestr = ';'.join(item for item in cookie)
    print(cookiestr)

    with open("cookies.txt","w") as f:
        f.writelines(cookiestr)
    return cookiestr



if __name__ == '__main__':
    gitlab_cookies()