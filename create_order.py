import configuration
import requests
import data

# создание нового заказа


def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH, json=body)

# получение трек-номера


def get_new_order_track():
    new_order_body = data.order_body
    resp_order = create_new_order(new_order_body)
    return resp_order.json()["track"]
