import requests
from requests.auth import HTTPBasicAuth
import json

request = ""

def getAccessToken():
    consumer_key = "ICneRzciMC5dMvMT4VvF3ZReivE2V2hd2z31CzgMam0qwVNR"
    consumer_secret = "tREluKtuIHG4SEHvdUz1v5twzku6Y4XlozpWy5sc6EeJ5DqqTJDrgT2x5biW8oUd"

    api_URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    res = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    # mpesa_access_token = json.loads(res.text)
    resp = res.json()

    # validated_mpesa_access_token = mpesa_access_token['access_token']
    print(resp)
    return resp

getAccessToken()
