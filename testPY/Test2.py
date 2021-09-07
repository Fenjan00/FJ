# -*- coding:utf-8 -*-

import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("http://docs.xinyu100.com/pcgo/android/daily/", headers=headers)
print(response.text)
