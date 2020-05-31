import tweepy
import sys
import urllib.request
import requests

import ssl
import json
import time


ssl._create_default_https_context = ssl._create_unverified_context


try:
  from urllib3 import PoolManager
  from json import loads as json
  from time import time
except:
  print("unable to import default modules")
  exit()

#Set constants
http = PoolManager()
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

class getbitcoin_price(object):

  def __init__(self, API_KEY):
      self.API_KEY = API_KEY
      if not self.API_KEY:
        print("No API key given. Register at pro.coinmarketcap.com")
        return
      self.api_data = self.grab(API_KEY)
      self.json = json(self.api_data)
      self.price = self.json['data'][0]['quote']['USD']['price']

  def grab(self, API_KEY):
      self.r = http.request("GET", URL, headers={
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': API_KEY}
      )
      return self.r.data.decode()








