from twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 200
PROMISED_UP = 100
ISP = ""

twitter_bot = InternetSpeedTwitterBot()
# Get current download/upload speeds from Speedtest.net
twitter_bot.get_internet_speed()

# Send tweet at ISP
tweet = f"Hey {ISP}, why is my internet speed {twitter_bot.down}  Mbps Down / {twitter_bot.up} Mbps Up?!\nWhen I pay for guaranteed speeds of {PROMISED_DOWN}/{PROMISED_UP}"

twitter_bot.tweet_at_provider(tweet)
