
import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer TbANcjsEjw0GWmqkRGtdDaMfMFw7'
}

payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwMjE5MjM1NDE1",
    "Timestamp": "20240219235415",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254708374149,
    "PartyB": 174379,
    "PhoneNumber": 254710568014,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "SSA",
    "TransactionDesc": "Payment of X" 
    }

response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
print(response.text.encode('utf8'))