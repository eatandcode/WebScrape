#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import sys
from importlib import reload
reload(sys)
#sys.setdefaultencoding('utf-8')



reddit = praw.Reddit(client_id='f8yDsjCFiBrLQA', \
client_secret='49aj9U54-bt9fxCPpI-eCpLYDUA', \
user_agent='scrape_bot', \
password='redditBOT$2019!')

subreddit = reddit.subreddit('malefashion')
top_subreddit = subreddit.top(limit=100)

for submission in subreddit.top(limit=1):
	print(submission.title, submission.id)


topics_dict = { "title":[], \
				"score":[], \
				"id":[], "url":[], \
				"comms_num": [], \
				"created": [], \
				"body":[]}

for submission in top_subreddit:
	topics_dict["title"].append(submission.title)
	topics_dict["score"].append(submission.score)
	topics_dict["id"].append(submission.id)
	topics_dict["url"].append(submission.url)
	topics_dict["comms_num"].append(submission.num_comments)
	topics_dict["created"].append(submission.created)
	topics_dict["body"].append(submission.selftext)
topics_data = pd.DataFrame(topics_dict)
topics_data_print = print(topics_dict)

def get_date(created):
	return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('scrape_bot_data.csv', index=False)

