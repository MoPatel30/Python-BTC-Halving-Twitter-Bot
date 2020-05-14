from sys import path
path.append('./')
from time import sleep
import tweepy
import mykey #import the file with your respective keys
import math


from twitterbot import getbitcoin_price


# Oauth keys
CONSUMER_KEY = mykey.BOT_CONSUMER_KEY
CONSUMER_SECRET = mykey.BOT_CONSUMER_SECRET
ACCESS_KEY = mykey.BOT_ACCESS_KEY
ACCESS_SECRET = mykey.BOT_ACCESS_SECRET

# Authentication with Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


#this should be your personal generated coinmarketcap (CMC) API key
API_KEY = "xxx" 

#btc price right before halving according to coinbase
price_before_halving = 8605.99

#differs based on which day it currently is post halving
which_day = 2

def main(days):
  query = getbitcoin_price(API_KEY)
  price = round(query.price, 2)
  net_change = round(price - price_before_halving, 2)
  
  percent_value = (round((price / price_before_halving),2) * 100.00) - 100.00
  finalLine = ""

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


#calls main once a day
while True:
  main(which_day)
  which_day += 1
  sleep(86400) 
  # happens to be once a day at 5pm central (3pm eastern)
 