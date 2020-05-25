


#quote bot account keys
BOT_CONSUMER_KEY = "TrNp5VoJFcEIldIb8ONliB0z4"
BOT_CONSUMER_SECRET = "ortokQhlZDEKkPLtblr74sbG75Ik1N64h8QRTJldsrGyuI4STA"
BOT_ACCESS_KEY = "1184238460888113152-GW0JSZI3GECoGpgy6STKfpIHuumGIa"
BOT_ACCESS_SECRET = "r2pJ9iunR8FOL2Xuj6Q7yy2sMDfKiJrGGY6eM54Zjp6cM"
CMC_API_KEY = "cdd3bcb4-0f36-4052-9476-ca56ad798e9d"




#import tweepy
#import time
#import sys
#import my_keys

#CONSUMER_KEY = my_keys.CONSUMER_KEY
#CONSUMER_SECRET = my_keys.CONSUMER_SECRET
#CCESS_KEY = my_keys.ACCESS_KEY
#ACCESS_SECRET = my_keys.ACCESS_SECRET

# The arg stuff can be confusing, but basically it means you set the
# file that the tweets are coming from at the time you run the Python
# script. So running the script looks like this:
# $ python tbot.py tweets.txt

# Connect to Twitter with the keys set above and the Tweepy library
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)


# Open tweets.txt and read it line by line into a big list
#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

# Go through the list (save to variable f) line by line
# First tweet the line, then wait 1200 seconds
#for line in f:
 #   api.update_status(status=line)
  #  time.sleep(6500)

# Note: if you run this script, it will immediately post a tweet to Twitter.
# If you cancel the running process and try to run it again, the script
# will open the file again and try to post the first tweet again.
# If it's already been posted, Twitter will return an error designed
# to prevent you from repeating past tweets. To fix this, remove
# any tweets that have already been posted from your tweets.txt
# file.

# Happy tweeting!
