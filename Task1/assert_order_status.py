import infoOrders

# 3. проверяем, что для третьего заказа все услуги обработаны И выполнено не меньше половины.
# Ну или по крайней мере на текущий момент возвращено не больше, чем выполнено,
# а ожидают возврат не больше, чем уже возвращено


# Проверяем третий элемент из массива "data"

order = infoOrders.info_orders["data"][2]

# если первая часть кода будет true, то дальше не пойдет. Если будет false, то он пойдет проверять по второму блоку кода
assert ((order["count"] == (order["completed"] + order["wait_refund"] + order["refunded"])) and (order["completed"] > order["count"] / 2)) or ((order["refunded"] < order["completed"]) or (order["wait_refund"] < order["refunded"]))
