import snscrape.modules.twitter as sntwitter
import pandas as pd

# scraper = twitterScraper.TwitterHashtagScraper("MediaLitWeek")

# for i, tweet in enumerate(scraper.get_items()):
#     if i > 2:
#         break
#     print(f"Tweet #{i} from {tweet.user}: {tweet.content}")

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#MediaLitWeek').get_items()):
    if i>10:
        break
    attributes_container.append([tweet.date.date(), tweet.likeCount, tweet.user.username, tweet.content])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Like Count", "User", "Tweets"])
print(tweets_df)