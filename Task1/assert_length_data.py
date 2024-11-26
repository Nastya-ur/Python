import infoOrders


# 1. проверяем, что заказы вообще есть в ответе от сервера

assert len(infoOrders.info_orders ["data"]) != 0
