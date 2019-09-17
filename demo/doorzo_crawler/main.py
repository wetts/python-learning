# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pymysql
import uuid
import bs4


def order_detail(req, order_id):
    order_uuid = str(uuid.uuid4()).replace("-", "")
    title = ""
    price = 0
    shop = None
    price_exchange_rate = 0
    postage_exchange_rate = None
    weight = None
    buy_time = None

    url_base = "https://www.doorzo.com/?n=Sig.Front.User.Order.DetailPage&Id="
    h = req.get(url_base + order_id)
    soup = BeautifulSoup(h.text, "html.parser")
    base_data_list = soup.find(
        "table", class_="table table-bordered").find_all("td")[1::2]

    buy_time = base_data_list[1].string.strip()

    if(base_data_list[3].string.strip()):
        weight = int(base_data_list[3].string.strip().replace("g", "")) / 1000

    b = soup.find("td", class_="font14").find_all("p")
    price_exchange_rate = b[4].contents[1].string
    price_exchange_rate = float(price_exchange_rate[6: -3].strip())
    postage_exchange_rate = price_exchange_rate
    postage_oversea_sum = int(
        b[6].contents[1].string[: -3].strip()) + int(b[7].contents[1].string[: -3].strip())

    t = soup.find(id='orderPostSuccess-ship')
    seller_name = t.find_all('span')[0].string.strip()
    if "mercari" in seller_name:
        shop = "94"
    elif "日亚自营" in seller_name:
        shop = "92"
    elif "雅虎拍卖" in seller_name:
        shop = "93"
    elif "日亚第三方" in seller_name:
        shop = "95"
    else:
        pass

    print(seller_name, weight, price_exchange_rate,
          buy_time, shop, postage_oversea_sum)

    sum = 0
    order_item_list = []
    for o in t.parent.next_siblings:
        if type(o) != bs4.element.NavigableString:
            order_item_uuid = str(uuid.uuid4()).replace("-", "")
            sum += 1
            d = o.find_all('td')
            order_item_title = d[1].contents[1].string.strip()
            order_item_price_oversea = int(
                d[2].string.replace("日元", "").strip())
            order_item_postage_oversea = 0
            order_item_service_fee_oversea = 0
            order_item_quantity = int(d[3].string.strip())
            order_item_press = "10"
            order_item_production = None
            if "ドラゴンボール" in order_item_title or "DRAGON BALL" in order_item_title:
                order_item_production = "2"
            elif "ワンピース" in order_item_title or "ONE PIECE" in order_item_title:
                order_item_production = "92"
            elif "僕のヒーローアカデミア" in order_item_title:
                order_item_production = "72"
            elif "カードキャプターさくら" in order_item_title:
                order_item_production = "4"
            elif "るろうに剣心" in order_item_title:
                order_item_production = "73"
            else:
                order_item_production = "-1"

            if shop == "94":
                if order_item_price_oversea > 1000:
                    order_item_service_fee_oversea = 150
                    order_item_price_oversea = order_item_price_oversea - order_item_service_fee_oversea
                else:
                    order_item_service_fee_oversea = 200
                    order_item_price_oversea = order_item_price_oversea - order_item_service_fee_oversea

            order_item_quality = "1" if shop == "92" else "2"
            order_item_price = (
                order_item_price_oversea + order_item_service_fee_oversea) * price_exchange_rate

            order_item_list.append(order_item(order_item_uuid, order_uuid, order_item_title, order_item_press, order_item_production, order_item_quantity,
                                              order_item_quality, order_item_price, order_item_price_oversea, order_item_postage_oversea, order_item_service_fee_oversea, buy_time))

    title = order_item_list[0].get_title()
    for oil in order_item_list:
        oil.set_postage_oversea(postage_oversea_sum / sum)
        p = oil.get_price() + postage_exchange_rate * oil.get_postage_oversea()
        oil.set_price(p)
        price += p

    o = order(order_uuid, title, price, 0, shop, weight, 2,
              price_exchange_rate, postage_exchange_rate, buy_time)

    # print(o)
    # for oil in order_item_list:
    #     print(oil)

    # 连接数据库
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 db='my_book_manage',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            o.save(cursor)
            for oil in order_item_list:
                oil.save(cursor)

        # 连接完数据库并不会自动提交，所以需要手动 commit 你的改动
        connection.commit()
    finally:
        connection.close()


def order_list(req, page_no):
    url_base = "https://www.doorzo.com/?Status=%E6%AD%A3%E5%9C%A8%E8%BF%9B%E8%A1%8C&n=Sig.Front.User.Order.ListPage&Page="
    h = req.get(url_base + page_no)


class order():
    def __init__(self, uuid, title, price, postage, shop, weight, service_provider_id, price_exchange_rate, postage_exchange_rage, buy_time):
        self.__uuid = uuid
        self.__title = title
        self.__price = price
        self.__postage = postage
        self.__shop = shop
        self.__weight = weight
        self.__service_provider_id = service_provider_id
        self.__price_exchange_rate = price_exchange_rate
        self.__postage_exchange_rage = postage_exchange_rage
        self.__buy_time = buy_time

    def save(self, cursor):
        sql = "INSERT INTO `tbl_order` (`uuid`, `title`, `price`, `postage`, `shop`, `weight`, `service_provider_id`, `price_exchange_rate`, `postage_exchange_rage`, `buy_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.__uuid, self.__title, self.__price, self.__postage, self.__shop, self.__weight,
                             self.__service_provider_id, self.__price_exchange_rate, self.__postage_exchange_rage, self.__buy_time))

    def __str__(self):  # 定义打印对象时打印的字符串
        return ' /// '.join(('%s:%s' % item for item in self.__dict__.items()))


class order_item():
    def __init__(self, uuid, order_uuid, title, press, production, quantity, quality, price, price_oversea, postage_oversea, service_fee_oversea, buy_time):
        self.__uuid = uuid
        self.__order_uuid = order_uuid
        self.__title = title
        self.__press = press
        self.__production = production
        self.__quantity = quantity
        self.__quality = quality
        self.__price = price
        self.__price_oversea = price_oversea
        self.__postage_oversea = postage_oversea
        self.__service_fee_oversea = service_fee_oversea
        self.__buy_time = buy_time

    def set_postage_oversea(self, postage_oversea):
        self.__postage_oversea = postage_oversea

    def get_postage_oversea(self):
        return self.__postage_oversea

    def get_title(self):
        return self.__title

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):  # 定义打印对象时打印的字符串
        return ' /// '.join(('%s:%s' % item for item in self.__dict__.items()))

    def save(self, cursor):
        sql = "INSERT INTO `tbl_order_item` (`uuid`, `order_uuid`, `title`, `press`, `production`, `quantity`, `quality`, `price`, `price_oversea`, `postage_oversea`, `service_fee_oversea`, `buy_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.__uuid, self.__order_uuid, self.__title, self.__press, self.__production, self.__quantity,
                             self.__quality, self.__price, self.__price_oversea, self.__postage_oversea, self.__service_fee_oversea, self.__buy_time))


if __name__ == '__main__':
    url0 = "https://www.doorzo.com/?n=Sig.Front.Front.LoginAction"
    url1 = "https://www.doorzo.com/?n=Sig.Front.User.Order.ListPage&Status=%E6%AD%A3%E5%9C%A8%E8%BF%9B%E8%A1%8C&Page=2"
    data = {'Email': "zhang.wetts@163.com",
            'Password': 'z87313141z'}
    # 进行登录，并保存cookie
    req = requests.Session()
    response = req.post(url0, data=data)
    zhuye = req.get(url1)

    soup = BeautifulSoup(zhuye.text, "html.parser")
    for l in soup.find("div", class_="right-width-container right").find("tbody").find_all("tr"):
        td_list = l.find_all("td")
        a_list = td_list[0].find_all("a")
        print(a_list)
        if len(a_list) == 0:
            order_detail(req, td_list[0].string.strip())
        else:
            for i in a_list:
                print("---", i.string)
                order_detail(req, i.string)
