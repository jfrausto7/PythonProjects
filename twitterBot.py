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

    # set equal to text
    tweetToTweet = tweetToTweet.text

    # remove all punctuation from tweet
    tweetToTweet = tweetToTweet.replace(',', '')
    tweetToTweet = tweetToTweet.replace('.', '')
    tweetToTweet = tweetToTweet.replace('…', '')
    tweetToTweet = tweetToTweet.replace('!', '')

    listOfText = tweetToTweet.split()

    # iterate through strings to remove link
    for s in listOfText:
        if len(s) > 4:
            if(s[0:4] == "http"):
                listOfText.remove(s)


    # shuffle words around add a capital and period
    random.shuffle(listOfText)
    if listOfText[0]:
        first = listOfText[0]
        first.capitalize()

    print(" ".join(listOfText) + ".")

    #status update with random tweet
    # api.update_status(" ".join(listOfText) + ".")


    print("Finished execution of TwitterBot.")

if __name__ == "__main__":
    getAndReturnRandom()








