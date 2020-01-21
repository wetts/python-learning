# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import bs4
import json
import time


if __name__ == '__main__':
    url0 = "https://www.doorzo.net/?n=Sig.Front.Front.LoginAction"
    url1 = "https://www.doorzo.net/?n=Sig.Front.User.UserMsg.GetUserLastMsgNum"
    data = {'Email': "zhang.wetts@163.com",
            'Password': 'z87313141z'}
    # 进行登录，并保存cookie
    req = requests.Session()
    response = req.post(url0, data=data)

    while 1000:
        zhuye = req.get(url1)
        print(json.loads(zhuye.text)['Count'])
        time.sleep(60)
