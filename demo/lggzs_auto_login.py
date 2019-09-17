# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url0 = "http://www.lggzs.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes"
data = {'username': "wetts",
        'password': 'z87313141z'}
# 进行登录，并保存cookie
req = requests.Session()
response = req.post(url0, data=data)

qd = req.get("http://www.lggzs.com/plugin.php?id=mpage_sign:sign&infloat=yes&handlekey=sign&inajax=1&ajaxtarget=fwin_content_sign")
soup = BeautifulSoup(qd.text)
v = soup.find('input', {"name": "formhash"})["value"]
print(v)

headers = {'content-type': 'charset=utf8'}
qd_data = {'formhash': v, 'handlekey': 'sign', 'signsubmit': 'yes',
           'moodid': '1', 'content': '记上一笔，hold住我的快乐！'.encode('gbk')}
qiandao = req.post(
    "http://www.lggzs.com/plugin.php?id=mpage_sign:sign", data=qd_data)

print(qiandao.text)
