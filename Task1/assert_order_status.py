import infoOrders

# 3. проверяем, что для третьего заказа все услуги обработаны И выполнено не меньше половины.
# Ну или по крайней мере на текущий момент возвращено не больше, чем выполнено,
# а ожидают возврат не больше, чем уже возвращено


# Проверяем третий элемент из массива "data"

i = infoOrders.info_orders["data"][2]
#assert (i["count"] == (i["completed"] + i["wait_refund"] + i["refunded"])) and (i["completed"] > i["count"] / 2)
#assert (i["refunded"] < i["completed"]) or (i["wait_refund"] < i["refunded"])

# есть мысли еще сделать так: если первая часть кода будет true, то дальше не пойдет. Если будет false, то он пойдет проверять по второму блоку кода
assert ((i["count"] == (i["completed"] + i["wait_refund"] + i["refunded"])) and (i["completed"] > i["count"] / 2)) or ((i["refunded"] < i["completed"]) or (i["wait_refund"] < i["refunded"]))
