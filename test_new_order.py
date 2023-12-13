import configuration
import requests
import create_order
import data


# получение заказа по трек номеру


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params=track)


def test_get_order_by_track():
    response_order = create_order.create_new_order(data.order_body)
    track = {"t": response_order.json()["track"]}
    response_order_by_track = get_order_by_track(track)
    assert response_order_by_track.status_code == 200

# Бакулина Софья, 11 поток — Финальный проект. Инженер по тестированию плюс
