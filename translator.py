import goslate
from twitter import *
from time import *

gs = goslate.Goslate()

OAUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# create empty arrays
owhtrans = []
dowhtrans = []

# get last 100 owh tweets, translate and push into an empty array
owhlatest = t.statuses.user_timeline(screen_name="owhnews",count=50)

for cowbell in owhlatest:
    trans = gs.translate(cowbell['text'].encode('utf-8'), 'nl')
    owhtrans.append(trans)

# get last 100 dutchowh tweets, push into empty array
dowhlatest = t.statuses.user_timeline(screen_name="dutchowh",count=50)
for monkey in dowhlatest:
    dowhtrans.append(monkey['text'].encode('utf-8'))

# find the differences and tweet 'em
diffs = list(set(owhtrans) - set(dowhtrans))

for items in reversed(diffs):
    stat = items[:140].replace("@","").replace("  "," ")
    print stat
    t.statuses.update(status=stat)
    sleep(10)
