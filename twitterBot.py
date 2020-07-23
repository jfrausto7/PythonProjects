#imports
from random import randint
import tweepy

# list to hold tweets in
tweets = []

def getAndReturnRandom():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("jL0Ces67FiDz6JIptpWPQbBzJ",
        "JI7EPhQqzYprMFo8fCayBgvckcJkVjYJkFxhctq54uAOtQSbuh")
    auth.set_access_token("1286432603533242368-58jpstN0IQdc6FZlJm6ZxaNKbWf6q8",
        "l4ymqoHzKStO3vJhb0uko9EQljSDmsGnrEhhDqsa8Hids")

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # get 20 recent tweets and store in tweets
    tweets = api.home_timeline();

    # get random number to select from tweets
    x = randint(0, len(tweets)-1)

    #setup of tweet to tweet
    tweetToTweet = tweets[x]
    if (tweetToTweet.retweeted) or ('RT @' in tweetToTweet.text):
        while((tweetToTweet.retweeted) or ('RT @' in tweetToTweet.text)):
            # get new random number to select from tweets
            x = randint(0, len(tweets) - 1)
            tweetToTweet = tweets[x]




    #status update with random tweet
    api.update_status(tweetToTweet.text)

    print("Finished execution of tweet.")

if __name__ == "__main__":
    getAndReturnRandom()








