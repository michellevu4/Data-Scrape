import snscrape.modules.twitter as twitterScraper

scraper = twitterScraper.TwitterHashtagScraper("MediaLitWeek")

for i, tweet in enumerate(scraper.get_items()):
    if i > 2:
        break
    print(f"Tweet #{i} from {tweet.user}: {tweet.content}")