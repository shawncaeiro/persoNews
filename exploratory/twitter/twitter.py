# Twitter functions
import tweepy
import json

keyFile = open("exploratory/twitter/keys.txt")
keyLines = keyFile.readlines()
keys = {
	"CK" : keyLines[0].strip(),
	"CS" : keyLines[1].strip(),
	"AT" : keyLines[2].strip(),
	"AS" : keyLines[3].strip()
}

auth = tweepy.OAuthHandler(keys["CK"], keys["CS"])
auth.set_access_token(keys["AT"], keys["AS"])

api = tweepy.API(auth)

user = api.get_user('twitter')
print user.screen_name
print user.followers_count

rate = api.rate_limit_status()
print json.dumps(rate, sort_keys=True,indent=4, separators=(',', ': '))
