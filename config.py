import os
from dotenv import load_dotenv
import datetime

try:
    postgres = os.environ['DATABASE_URL']
    token = os.environ['TOKEN']
    print(os.environ['TZ'])
    client_id = os.environ['client_id']
    client_secret = os.environ['client-secret']
    print("time is ", datetime.datetime.now())
    print('loaded heroku env variables')

except KeyError:
    load_dotenv()
    print('loaded local dotenv file')
    postgres = os.environ['uri']
    token = os.environ['token']
    client_id = os.environ['client-id']
    client_secret = os.environ['client-secret']
