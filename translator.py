import goslate
from twitter import *
from time import *
from datetime import *

gs = goslate.Goslate()

OAUTH_TOKEN = 'XXXXXXXXXXXXX'
OAUTH_SECRET = 'XXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXX'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#create new list
owhnew = []

# get timestamp of last dutchOWH tweet
dowhlatest = t.statuses.user_timeline(screen_name="dutchowh",count=1)
thendowh = dowhlatest[0]['created_at']
ds = datetime.strptime(thendowh, '%a %b %d %H:%M:%S +0000 %Y')

# get last 100 owh tweets, translate each and tweet the ones posted after last dutchOWH tweet
owhlatest = t.statuses.user_timeline(screen_name="owhnews",count=100)

# loop through list
for z in reversed(owhlatest):
    
    # translate, grab timestamp
    trans = gs.translate(z['text'], 'nl')
    ts = datetime.strptime(z['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    
    # email fix
    edittweet = trans.replace(" @ owh.com","@owh.com").replace("  "," ").strip()

    # skip tweets > 140 characters and older than last dutchOWH tweet
    if len(edittweet) < 140 and ts > ds:
        print edittweet
        try:
            owhnew.append(edittweet)
            t.statuses.update(status=edittweet)
        except TwitterHTTPError as e:
            print "Something went wrong with this one. Skipping ..."
            pass
        sleep(10)
    else:
        pass
        
print "Tweeted " + str(len(owhnew)) + " things."
