import goslate
from twitter import *
from time import *

gs = goslate.Goslate()

OAUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXX'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# empty arrays
owhtrans = []
dowhtrans = []

# get last 100 owh tweets, push into empty array
owhlatest = t.statuses.user_timeline(screen_name="owhnews",count=100)

for thing in owhlatest:
    trans = gs.translate(thing['text'].encode('utf-8'), 'nl')   
    owhtrans.append(trans)

# get last 100 dutchowh tweets, push into empty array
dowhlatest = t.statuses.user_timeline(screen_name="dutchowh",count=100)

for monkey in dowhlatest:
    dowhtrans.append(monkey['text'])

# find the differences and tweet 'em
diffs = [x for x in owhtrans if x not in dowhtrans]

for items in reversed(diffs):
    t.statuses.update(status=items[:140])
    sleep(10)
