import infoOrders
import pprint

# словарь total_info_orders

operator = ("your_email@mail.ru","your_name")
#print(operator)

id_orders = []
for order in infoOrders.info_orders["data"] :
    id_orders.append(order["_id"])
id_orders.append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")
#print(id_orders)

orders = {
        "completed": sum (order ["completed"] for order in infoOrders.info_orders ["data"]),
        "wait_refund" : sum (order ["wait_refund"] for order in infoOrders.info_orders ["data"]),
        "refunded" : sum (order ["refunded"] for order in infoOrders.info_orders ["data"])
}
#print(orders)

total_info_orders = {
    "operator" : operator,
    "id_orders" : id_orders,
    "orders" : orders
}
pprint.pprint(total_info_orders)


