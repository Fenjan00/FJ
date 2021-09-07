#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import qrcode
from bs4 import BeautifulSoup
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("http://docs.xinyu100.com/pcgo/android/daily/", headers=headers)


htmlres=str(response.text).splitlines()



#安卓最新包QRcode
andorid_pkglist={}

def andorid_pkg(version):
    for line in htmlres:
        try:
            if str(line[1]) == 'a':
                pkgname=str(line).split('<a href="')[1].split('/"')[0]
                pkgumb=pkgname.split('SNAPSHOT.')[1]         
                if int(pkgumb)>0:
                    andorid_pkglist[pkgname]=pkgumb
        except:
            pass

    print (andorid_pkglist)


    if version==0:
        andorid_newpkg_url="http://docs.xinyu100.com/pcgo/android/daily/"+str(max(andorid_pkglist, key=andorid_pkglist.get))+"/"+"Caiji.V"+str(max(andorid_pkglist, key=andorid_pkglist.get))+".apk"
        andorid_newpkg_name="Caiji.V"+str(max(andorid_pkglist, key=andorid_pkglist.get))+".apk"

        img=qrcode.make(andorid_newpkg_url)
        img.save("./pkg.jpg")

        return andorid_newpkg_url,andorid_newpkg_name
    else:
        for k,v in andorid_pkglist.items():
            if int(v) == version:
                print (k,v)
                andorid_newpkg_name="Caiji.V"+str(k)+".apk"
                andorid_newpkg_url="http://docs.xinyu100.com/pcgo/android/daily/"+str(k)+"/"+"Caiji.V"+str(k)+".apk"
                img = qrcode.make(andorid_newpkg_url)
                img.save("./pkg.jpg")

                return andorid_newpkg_url,andorid_newpkg_name


if __name__ == '__main__':
    andorid_pkg(0)
    andorid_newpkg_url,andorid_newpkg_name=andorid_pkg(0)
    print(andorid_newpkg_url)
    print (andorid_newpkg_name)
