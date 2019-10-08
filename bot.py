import json
import time
import requests
import nicehash
import http.client
from time import sleep
from datetime import datetime, timedelta


def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config

# https://github.com/nicehash/rest-clients-demo
host = 'https://api2.nicehash.com'
organisation_id = get_config()["nicehash_organization_id"]
key = get_config()["nicehash_api_key"]
secret = get_config()["nicehahs_api_secret"]
private_api = nicehash.private_api(host, organisation_id, key, secret)
public_api = nicehash.public_api(host, True)
exchange_info = public_api.get_exchange_markets_info()

last_start = datetime.utcnow()


def discord_send_message(notification):

    webhookurl = get_config()["discord_webhook_url"]

    formdata = (
        '------:::BOUNDARY:::\r\nContent-Disposition: form-data; name="content"\r\n\r\n'
        + notification
        + "\r\n------:::BOUNDARY:::--"
    )
    try:
        connection = http.client.HTTPSConnection("discordapp.com")
        connection.request(
            "POST",
            webhookurl,
            formdata,
            {
                "content-type": "multipart/form-data; boundary=----:::BOUNDARY:::",
                "cache-control": "no-cache",
            },
        )

        response = connection.getresponse()

    except requests.exceptions.RequestException as e:
        pass
#        print((str(e)))
    except Exception as e:
        pass
#        print((str(e)))

def get_balance(coin):
    # BTC = 0
    # XRP = 2
    return private_api.get_accounts()[coin]["balance"]


def make_trade():

    discord_send_message(f'BTC balance before trade is {get_balance(0)}')
    discord_send_message(f'XRP balance before trade is {get_balance(2)}')

    try:
        new_buy_market_order = private_api.create_exchange_buy_market_order(exchange_info['symbols'][1]['symbol'], private_api.get_accounts()[0]["balance"])
    except Exception as e:
        discord_send_message(str(e))

    discord_send_message(f'Bought {new_buy_market_order["executedQty"]} XRP')
    discord_send_message(f'Total XRP balance after trade is {get_balance(2)}')


def main():

    global last_start

    discord_send_message("Starting ...")

    if get_balance(0) > 0:
        make_trade()

    while True:
        if last_start + timedelta(hours=float(get_config()["exchange_period_hours"])) < datetime.utcnow():
            make_trade()
            last_start = datetime.utcnow()
            time.sleep(3600)
            continue
        else:
            time.sleep(3600)
            continue




if __name__ == "__main__":
    main()
