import requests
import json
import time
import conf1
def price_check():
    url = "https://min-api.cryptocompare.com/data/price"
    querystring = {"fsym":"BTC","tsyms":"INR"}
    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    current_price = response['INR']
    return current_price



def send_telegram_message(message):

    url = "https://api.telegram.org/" + conf1.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf1.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram response")
         print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False


while True:
    market_price = price_check()
    print ('market price is: ',market_price)
    print ('Selling price is: ',conf1.threshold)
    time.sleep(10)
    if market_price > conf1.threshold:
        print("market price exceeded")
        message = "Bitcoin Value exceeded from "+str(conf1.threshold)+"/new val$
        telegram_status = send_telegram_message(message)
        time.sleep(60)
