import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
mediaLitWeek = []

print("#MediaLitWeek")
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#MediaLitWeek').get_items()):
    if i>10:
        break
    mediaLitWeek.append([tweet.date.date(), tweet.place, tweet.likeCount, tweet.retweetCount, tweet.inReplyToUser, tweet.user.username, tweet.user.displayname, tweet.user.rawDescription, tweet.user.followersCount, tweet.user.verified, tweet.content])

# Creating a dataframe from the tweets list above
mediaDF = pd.DataFrame(mediaLitWeek, columns=["Date Created", "Location", "Like Count", "Retweet Count", "In Reply To", "User", "User Name", "User Description", "Follower Count", "Verified", "Tweets"])
print(mediaDF)

# Created a list to append all tweet attributes(data)
digCitWeek = []

print("#DigCitWeek")
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#DigCitWeek').get_items()):
    if i>10:
        break
    digCitWeek.append([tweet.date.date(), tweet.place, tweet.likeCount, tweet.retweetCount, tweet.inReplyToUser, tweet.user.username, tweet.user.displayname, tweet.user.rawDescription, tweet.user.followersCount, tweet.user.verified, tweet.content])

# Creating a dataframe from the tweets list above
digDF = pd.DataFrame(digCitWeek, columns=["Date Created", "Location", "Like Count", "Retweet Count", "In Reply To", "User", "User Name", "User Description", "Follower Count", "Verified", "Tweets"])
print(digDF)

# export the dataframe to a csv file if desired
mediaDF.to_csv("#MediaLitWeek.csv")
digDF.to_csv("#DigCitWeek.csv")