import csv
from storage import all_articles

all_articles = all_articles[all_articles['eventType'] == "CONTENT SHARED"]

all_articles.head(5)

def total_events(article):
  total_likes = all_articles[(all_articles['eventType'] == article['contentId']) & (all_articles['eventType'] == 'LIKE')].shape[0]
  total_views = all_articles[(all_articles['eventType'] == article['contentId']) & (all_articles['eventType'] == 'VIEW')].shape[0]
  total_comments = all_articles[(all_articles['eventType'] == article['contentId']) & (all_articles['eventType'] == 'COMMENT')].shape[0]
  total_bookmarks = all_articles[(all_articles['eventType'] == article['contentId']) & (all_articles['eventType'] == 'BOOKMARK')].shape[0]
  total_follows = all_articles[(all_articles['eventType'] == article['contentId']) & (all_articles['eventType'] == 'FOLLOW')].shape[0]

  return total_likes+total_views+total_comments+total_bookmarks+total_follows

all_articles['Total events'] = all_articles.apply(total_events,axis=1)
all_articles.head(5)