import infoOrders
from itertools import count
from wsgiref.validate import assert_

# 1. проверяем, что заказы вообще есть в ответе от сервера

# отдельно в каждом массиве проверяем, что count > 0

assert infoOrders.info_orders ["data"][0]["count"] > 0
assert infoOrders.info_orders ["data"][1]["count"] > 0
assert infoOrders.info_orders ["data"][2]["count"] > 0

# попытка сделать это через цикл, вопрос про i - это мы получается вводим в процессе цикла новую переменную??

for i in infoOrders.info_orders["data"] :
    assert i ["count"] != 0