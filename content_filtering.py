from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

article = pd.read_csv('articles.csv')
article = article[article['Category'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(article['Category'])

similarilty = cosine_similarity(count_matrix,count_matrix)

article = article.reset_index()
indices = pd.Series(article.index, index=article['title'])

def get_recomendation(title):
    idx = indices[title]
    similar = list(enumerate(similarilty[idx]))
    return['title']
