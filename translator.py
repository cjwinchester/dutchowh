import goslate
from twitter import *

gs = goslate.Goslate()

OAUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXX'
OAUTH_SECRET = 'XXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXX'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

latest = t.statuses.user_timeline(screen_name="owhnews",count=1)

thing = latest[0]['text']

trans = gs.translate(thing, 'nl')

t.statuses.update(status=trans)
