import json
import time
import requests
import nicehash
import http.client
from time import sleep
from datetime import datetime, timedelta



last_start = datetime.utcnow()



def check_time():

    global last_start

    if last_start + timedelta(hours=float(get_config()["exchange_period_hours"])) < datetime.utcnow():
        return True



def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config



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



def make_trade():

    # https://github.com/nicehash/rest-clients-demo
    host = 'https://api2.nicehash.com'
    organisation_id = get_config()["nicehash_organization_id"]
    key = get_config()["nicehash_api_key"]
    secret = get_config()["nicehahs_api_secret"]

    private_api = nicehash.private_api(host, organisation_id, key, secret)
    public_api = nicehash.public_api(host, True)

    exchange_info = public_api.get_exchange_markets_info()

    # current_market = exchange_info['symbols'][1]['symbol'] # XRPBTC
    # btc_balance = private_api.get_accounts()[0]["balance"] # BTC balance

    new_buy_market_order = private_api.create_exchange_buy_market_order(exchange_info['symbols'][1]['symbol'], private_api.get_accounts()[0]["balance"])

    discord_send_message(f'Bought {new_buy_market_order["executedQty"]} XRP')
    discord_send_message(f'Balance now is {private_api.get_accounts()[2]["balance"]} XRP')



def main():

    discord_send_message("Starting ...")

    global last_start

    while True:
        if check_time() != True:
            time.sleep(3600)
            continue
        else:
            make_trade()
            last_start = datetime.utcnow()
            time.sleep(3600)
            continue



if __name__ == "__main__":
    main()
