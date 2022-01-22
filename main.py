from crypt import methods
from flask import Flask,jsonify,request
from storage import liked_articles,disliked_articles,all_articles

app = Flask(__name__)

@app.route('/get-article')
def get_article():
 return jsonify({
     'data' : all_articles[0],
     'activity' : all_articles[0][3] ,
     'status' : 'Success'
 }),201

@app.route('/liked-article',methods=['POST'])
def liked_article():
 article = all_articles[0]
 liked_articles.append(article)
 all_articles.pop(0)
 return jsonify({
     'status' : 'Success'
 }),201

@app.route('/disliked-article',methods=['POST'])
def disliked_article():
 article = all_articles[0]
 disliked_articles.append(article)
 all_articles.pop(0)
 return jsonify({
     'status' : 'Success'
 }),201

if __name__ ==  '__main__':
 app.run()