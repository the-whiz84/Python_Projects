# Extra Credit:

# The PayScale dataset used in this lesson was from 2008 and looked at the prior 10 years. Notice how Finance ranked very high on post-degree earnings at the time. However, we all know there was a massive financial crash in that year. Perhaps things have changed. Can you use what you've learnt about web scraping in the prior lessons (e.g., Day 45) and share some updated information from PayScale's website in the comments below? 


import pandas as pd
import requests
from io import StringIO

# get html data
url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
header = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15",
  "sec-fetch-dest": "document",
  "Accept-Language": "en-US,en;q=0.9",
  "X-Requested-With": "XMLHttpRequest"
}
html_data = requests.get(url, headers=header)

# create data frame by importing html data
df = pd.read_html(StringIO(html_data.text))[0]

# clean up data frame
df = df.drop('Rank', axis=1)
df.loc[:,'Major'] = df['Major'].str.replace('Major:', '')
df.loc[:,'Degree Type'] = df['Degree Type'].str.replace('Degree Type:', '')
df.loc[:,'Early Career Pay'] = df['Early Career Pay'].str.replace('Early Career Pay:', '')
df.loc[:,'Mid-Career Pay'] = df['Mid-Career Pay'].str.replace('Mid-Career Pay:', '')
df.loc[:,'% High Meaning'] = df['% High Meaning'].str.replace('% High Meaning:', '')

# get clean Data Frame
print(df.head())

#                                               Major Degree Type Early Career Pay Mid-Career Pay % High Meaning
# 0                             Petroleum Engineering   Bachelors          $98,100       $212,100            60%
# 1      Operations Research & Industrial Engineering   Bachelors         $101,200       $202,600            21%
# 2  Electrical Engineering & Computer Science (EECS)   Bachelors         $128,500       $192,300            45%
# 3                                Interaction Design   Bachelors          $77,400       $178,800            55%
# 4                                  Building Science   Bachelors          $71,100       $172,400            46%