from sys import path
#path.append('./')
from time import sleep
import tweepy
import math

from datetime import date, timedelta

from os import environ
from twitterbot import getbitcoin_price


# Oauth keys
#using environ and heroku config vars to keep my API keys secure
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# CoinMarketCap API Key
API_KEY = environ['CMC_API_KEY']


# Authentication with Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



price_before_halving = 8605.99

# Current day for tweeting when uploaded to heroku
# increments by one every 24hrs



# function that does all the magic

query = getbitcoin_price(API_KEY)
price = round(query.price, 2)
net_change = round(price - price_before_halving, 2)
  

value = price / price_before_halving
value = value * 100.00

percent_value = round(value, 2)
percent_value = round(percent_value - 100.00, 2)


finalLine = ""



today = date.today()

yesterday = today - timedelta(days = 1)

currentDate = yesterday.strftime("%B %d, %Y")



# what the tweet will say if the price has increased since halving
if query.price > price_before_halving:
  line = "3rd Halving Date: May 11, 2020" + "\n"
  lineZero =  "Current Date: " + currentDate + "\n" + "\n"
  lineOne = "Bitcoin price at halving: $%s" % price_before_halving + "\n"
  lineTwo = "Bitcoin price currently:  $%s" % price + "\n"
  lineHalf = "Change in price: +$%s" % net_change + "\n" + "\n"
  lineThree = "#Bitcoin is up %s" % percent_value  + "% since the halving!"  + "\n" + "\n"
  lineFour = "📈🚀" 

  finalLine =  line + lineZero + lineOne + lineTwo + lineHalf + lineThree + lineFour
  api.update_status(status=finalLine)
 

  # what the tweet will say if the price has decreased since halving
else:
  line = "3rd Halving Date: May 11th, 2020" + "\n"
  lineOne =  "Current Date: " + currentDate + "\n" + "\n"
  lineOne = "Bitcoin price at halving: $%s" % price_before_halving + "\n"
  lineTwo = "Bitcoin price currently:  $%s" % price + "\n"
  lineHalf = "Change in price: -$%s" % net_change + "\n" + "\n"
  lineThree = "#Bitcoin is down %s" % percent_value + "% since the halving" + "\n" + "\n"
  lineFour = "📉🙁"

  finalLine =  line + lineZero + lineOne + lineTwo + lineHalf + lineThree + lineFour
  api.update_status(status=finalLine)
  

sleep(86402)
