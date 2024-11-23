import infoOrders

# 2. проверяем, что время выполнение первого и второго заказов не превышает 6 часов

assert infoOrders.info_orders ["data"][0]["delay"] <= 6
assert infoOrders.info_orders ["data"][1]["delay"] <= 6

# проверить, это через цикл

for i in infoOrders.info_orders ["data"][:2]:
    assert i["delay"] <= 6