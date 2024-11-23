import infoOrders
import pprint

# словарь total_info_orders

operator = ("your_email@mail.ru","your_name")
#print(operator)

id_orders = []
for i in infoOrders.info_orders["data"] :
    id_orders.append(i["_id"])
id_orders.append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")
#print(id_orders)

orders = {
        "completed": sum (i ["completed"] for i in infoOrders.info_orders ["data"]),
        "wait_refund" : sum (i ["wait_refund"] for i in infoOrders.info_orders ["data"]),
        "refunded" : sum (i ["refunded"] for i in infoOrders.info_orders ["data"])
}
#print(orders)

total_info_orders = {
    "operator" : operator,
    "id_orders" : id_orders,
    "orders" : orders
}
pprint.pprint(total_info_orders)


