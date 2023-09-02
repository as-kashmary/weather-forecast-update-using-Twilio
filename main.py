import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os



account_sid = "Your Twilio Account Sid"
auth_token = "Your Twilio Account auth token"



param={
    "lat":"Your Home Addresse's Latitude",
    "lon":"Your Home Addresse's Longitude",
    "appid":"Your api key from https://home.openweathermap.org/api_keys"

}



response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast?",params=param)
for i in range(0,4):
    k=response.json()["list"][i]["weather"][0]["id"];
    time=response.json()["list"][i]["dt_txt"]
    if k <700:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token,http_client=proxy_client)
        message = client.messages.create(
            from_="Your Twilio phone number",
            body="It will rain today",
            to="Your phone number used to register in Twilio"

        )
        break;




