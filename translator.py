import goslate
from twitter import *
from time import *

gs = goslate.Goslate()

OAUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXX'
OAUTH_SECRET = 'XXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXX'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# create two empty lists
owhtrans = []
dowhtrans = []

# get last 50 owh tweets, translate each and push them into empty list
owhlatest = t.statuses.user_timeline(screen_name="owhnews",count=50)

for cowbell in owhlatest:
    trans = gs.translate(cowbell['text'].encode('utf-8'), 'nl')
    if len(trans) <= 140:
        edittweet = trans.replace("@","").replace("  "," ").strip()
        owhtrans.append(edittweet)
    else:
        pass

# get last 50 dutchowh tweets, push into empty array
dowhlatest = t.statuses.user_timeline(screen_name="dutchowh",count=50)
for monkey in dowhlatest:
    dowhtrans.append(monkey['text'].encode('utf-8'))

# for find the differences, tweet 'em in reverse order
diffs = list(set(owhtrans) - set(dowhtrans))

for items in reversed(diffs):
    if len(items) <= 140:
        stat = items.replace("@","").replace("  "," ").strip()
        print stat
        t.statuses.update(status=stat)
    else:
        pass
    sleep(10)
