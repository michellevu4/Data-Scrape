import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

print("#MediaLitWeek")
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#MediaLitWeek').get_items()):
    if i>10:
        break
    attributes_container.append([tweet.date.date(), tweet.place, tweet.coordinates.longitude, tweet.Coordinates.latitude, tweet.likeCount, tweet.retweetCount, tweet.inReplyToUser, tweet.user.username, tweet.user.displayname, tweet.user.rawDescription, tweet.user.followersCount, tweet.user.verified, tweet.content])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Location", "Longitude", "Latitude", "Like Count", "Retweet Count", "In Reply To", "User", "User Name", "User Description", "Follower Count", "Verified", "Tweets"])
print(tweets_df)

# Created a list to append all tweet attributes(data)
attributes_container2 = []

print("#DigCitWeek")
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#DigCitWeek').get_items()):
    if i>10:
        break
    attributes_container2.append([tweet.date.date(), tweet.place, tweet.coordinates.longitude, tweet.Coordinates.latitude, tweet.likeCount, tweet.retweetCount, tweet.inReplyToUser, tweet.user.username, tweet.user.displayname, tweet.user.rawDescription, tweet.user.followersCount, tweet.user.verified, tweet.content])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(attributes_container2, columns=["Date Created", "Location", "Longitude", "Latitude", "Like Count", "Retweet Count", "In Reply To", "User", "User Name", "User Description", "Follower Count", "Verified", "Tweets"])
print(tweets_df)

# export the dataframe to a csv file if desired
mediaDF.to_csv("#MediaLitWeek.csv")
digDF.to_csv("#DigCitWeek")