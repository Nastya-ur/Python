
'''
count - кол-во услуг всего в заказе
completed/wait_refund/refunded - статусы обработанных услуг в конкретном заказе.
Если значение 0 - значит нет услуг в этом заказе подходящее под этот статус
т.е. услуга может быть выполненной, возвращенной или ожидающей возврата`

delay - кол-во часов между выполнениями услуг
'''
from itertools import count
from wsgiref.validate import assert_

# поместили в переменную следующий словарь (json)

info_orders = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}


# 1. проверяем, что заказы вообще есть в ответе от сервера

# отдельно в каждом массиве проверяем, что count > 0

assert info_orders ["data"][0]["count"] > 0
assert info_orders ["data"][1]["count"] > 0
assert info_orders ["data"][2]["count"] > 0

# попытка сделать это через цикл, вопрос про i - это мы получается вводим в процессе цикла новую переменную??

for i in info_orders["data"] :
    assert i ["count"] != 0

# тут попытка понять, как посчитать кол-во заказов в тотале

total_count = sum (i ["count"] for i in info_orders ["data"])
print(total_count)

# 2. проверяем, что время выполнение первого и второго заказов не превышает 6 часов

assert info_orders ["data"][0]["delay"] <= 6
assert info_orders ["data"][1]["delay"] <= 6

# проверить, это через цикл

for i in info_orders ["data"][:2]:
    assert i["delay"] <= 6

# 3. проверяем, что для третьего заказа все услуги обработаны И выполнено не меньше половины.
# Ну или по крайней мере на текущий момент возвращено не больше, чем выполнено,
# а ожидают возврат не больше, чем уже возвращено


# Проверяем третий элемент из массива "data"

i = info_orders["data"][2]
assert (i["count"] == (i["completed"] + i["wait_refund"] + i["refunded"])) and (i["completed"] > i["count"] / 2)
assert (i["refunded"] < i["completed"]) or (i["wait_refund"] < i["refunded"])

# есть мысли еще сделать так: если первая часть кода будет true, то дальше не пойдет. Если будет false, то он пойдет проверять по второму блоку кода
assert ((i["count"] == (i["completed"] + i["wait_refund"] + i["refunded"])) and (i["completed"] > i["count"] / 2)) or ((i["refunded"] < i["completed"]) or (i["wait_refund"] < i["refunded"]))


# словарь total_info_orders

operator = ("your_email@mail.ru","your_name")
#print(operator)

id_orders = []
for i in info_orders["data"] :
    id_orders.append(i["_id"])
id_orders.append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")
#print(id_orders)

orders = {
        "completed": sum (i ["completed"] for i in info_orders ["data"]),
        "wait_refund" : sum (i ["wait_refund"] for i in info_orders ["data"]),
        "refunded" : sum (i ["refunded"] for i in info_orders ["data"])
}
#print(orders)

total_info_orders = {
    "operator" : operator,
    "id_orders" : id_orders,
    "orders" : orders
}
print(total_info_orders)








