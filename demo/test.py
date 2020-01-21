# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/11/17 11:33:04
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   实验室规章【自动做题】
'''

# here put the import lib


import requests
from bs4 import BeautifulSoup
import json

# test_modle = 'mn_test'
test_modle = 'zs_test'

url0 = "http://aqjy.ccnu.edu.cn/LabTest/labtest/getuserInfo"
data = {'username': "刘栋",
        'password': '2019124097'}
# 进行登录，并保存cookie
req = requests.Session()
response = req.post(url0, data=json.dumps(data))
print(response.text)

f = req.get("http://aqjy.ccnu.edu.cn/LabTest/labtest/mnTestOrzsTest")
print(f.text)

s = req.get("http://aqjy.ccnu.edu.cn/LabTest/labtest/starttest")

headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7', 'Host': 'aqjy.ccnu.edu.cn', 'Origin': 'http://aqjy.ccnu.edu.cn', 'Referer': 'http://aqjy.ccnu.edu.cn/LabAnquanTest/danxuantest.jsp',
           'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
qd = req.post("http://aqjy.ccnu.edu.cn/LabTest/labtest/getpaperInfo/单选", headers=headers)
# print(qd.text)


qd1 = req.post("http://aqjy.ccnu.edu.cn/LabTest/labtest/calculateScores")
print(qd1.text)

true_ans = json.loads(qd1.text)
ans = {'danxuan_ans': true_ans.get('danxuan_true_ans'), 'duoxuan_ans':  true_ans.get('duoxuan_true_ans'), 'panduan_ans': true_ans.get('panduan_true_ans'), 'test_modle': test_modle}
qd2 = req.post("http://aqjy.ccnu.edu.cn/LabTest/labtest/submitAns", data=json.dumps(ans))
print(qd2.text)

sc = {'danxuan_mark': '40', 'duoxuan_mark': '20', 'panduan_mark': '40', 'all_mark': '100', 'test_modle': test_modle}
h2 = {'Content-Type': 'application/json'}
qd3 = req.post("http://aqjy.ccnu.edu.cn/LabTest/labtest/insert_score", headers=h2, data=json.dumps(sc))
print(qd3.text)
