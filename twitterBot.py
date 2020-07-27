#!/usr/bin/python

#imports
from random import randint
import random
import tweepy

"""This method is the entire purpose of this """
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

    # get 200 recent tweets and store in tweets
    tweets = api.home_timeline(count=200)

    # get random number to select from tweets
    x = randint(0, len(tweets)-1)

    #setup of tweet to tweet
    tweetToTweet = tweets[x]
    if (tweetToTweet.retweeted) or ('RT @' in tweetToTweet.text) or len(tweetToTweet.text.split()) > 21:
        while((tweetToTweet.retweeted) or ('RT @' in tweetToTweet.text) or len(tweetToTweet.text.split()) > 21):
            # get new random number to select from tweets
            x = randint(0, len(tweets) - 1)
            tweetToTweet = tweets[x]


    # set equal to text
    tweetToTweet = tweetToTweet.text

    # remove all punctuation from tweet
    tweetToTweet = tweetToTweet.replace(',', '')
    tweetToTweet = tweetToTweet.replace('.', '')
    tweetToTweet = tweetToTweet.replace('…', '')
    tweetToTweet = tweetToTweet.replace('!', '')
    tweetToTweet = tweetToTweet.replace('?', '')
    tweetToTweet = tweetToTweet.replace('“', '')
    tweetToTweet = tweetToTweet.replace("&amp", '&')

    listOfText = tweetToTweet.split()

    # iterate through strings to remove link
    for s in listOfText:
        if len(s) > 4:
            if(s[0:4] == "http"):
                listOfText.remove(s)

    # iterate through strings to make all lowercase
    for i in range(len(listOfText)):
        listOfText[i] = listOfText[i].lower()

    # shuffle words around add a capital and period
    random.shuffle(listOfText)
    if listOfText[0]:
        listOfText[0] = listOfText[0].capitalize()

    string = " ".join(listOfText) + "."

    #status update with random tweet
    api.update_status(string)

    try:
        print("Tweeted: " + string)
        print("Finished execution of TwitterBot.")
    except:
        pass

if __name__ == "__main__":
    getAndReturnRandom()








