import infoOrders
from datetime import datetime, timedelta

# 2. проверяем, что время выполнение первого и второго заказов не превышает 6 часов

for order in infoOrders.info_orders["data"][:2]:
    started_at_dt = datetime.strptime(order["startedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
    completed_at_dt = datetime.strptime(order["completedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
    time_difference = completed_at_dt - started_at_dt

    assert time_difference <= timedelta(hours=6)






