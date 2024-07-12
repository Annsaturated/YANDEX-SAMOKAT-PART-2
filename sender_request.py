import requests
import config
import data

def post_new_order(order_body):
    return requests.post(config.URL_SERVER + config.CREATE_ORDER,
                         headers=data.headers,
                         json=order_body)

def get_order_track(track):
    return requests.get(config.URL_SERVER + config.CREATE_ORDER + '?t=' + str(track),
                        headers=data.headers)