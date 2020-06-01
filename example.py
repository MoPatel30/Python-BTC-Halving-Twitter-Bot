from sys import path
#path.append('./')
from time import sleep
import tweepy

import math

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
which_day = 20


# function that does all the magic
def main(days):
  query = getbitcoin_price(API_KEY)
  price = round(query.price, 2)
  net_change = round(price - price_before_halving, 2)
  

  value = price / price_before_halving
  value = value * 100.00

  percent_value = round(value, 2)
  percent_value = round(percent_value - 100.00, 2)
  #value = (price * 100) / price_before_halving
  #percent_value = round((value / 10), 2)
  finalLine = ""
  
  # what the tweet will say if the price has increased since halving
  if query.price > price_before_halving:
    lineZero = "Days since 3rd #Bitcoin halving: %s" % days + "\n" + "\n"
    lineOne = "Bitcoin price at halving: $%s" % price_before_halving + "\n"
    lineTwo = "Bitcoin price currently:  $%s" % price + "\n" + "\n"
    lineHalf = "Change in price: +$%s" % net_change + "\n" + "\n"
    lineThree = "#Bitcoin is up %s" % percent_value  + "% since the halving!"  + "\n" + "\n"
    lineFour = "📈🚀" 

    finalLine = lineZero + lineOne + lineTwo + lineHalf + lineThree + lineFour
    api.update_status(status=finalLine)
    days += 1

  # what the tweet will say if the price has decreased since halving
  else:
    lineZero = "Days since 3rd #Bitcoin halving: %s" % days + "\n" + "\n"
    lineOne = "Bitcoin price at halving: $%s" % price_before_halving + "\n"
    lineTwo = "Bitcoin price currently:  $%s" % price + "\n" + "\n"
    lineHalf = "Change in price: -$%s" % net_change + "\n" + "\n"
    lineThree = "#Bitcoin is down %s" % percent_value + "% since the halving" + "\n" + "\n"
    lineFour = "📉🙁"

    finalLine = lineZero + lineOne + lineTwo + lineHalf + lineThree + lineFour
    api.update_status(status=finalLine)
    days += 1


# To keep in loop and tweet once a day
while True:
  main(which_day)
  sleep(86400) 
  which_day += 1
  
  
  
