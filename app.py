from flask import Flask, render_template, Blueprint,redirect,url_for
from list_tweets import list_all_tweets
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for('.get_tweet'))

@app.route("/tweet")
def get_tweet():
    name = "geeksambhu"
    tweet_list= list_all_tweets(name)
    return render_template("tweet_index.html", tweets=tweet_list, name=name)

@app.route("/insta")
def get_insta():
    name="geeksambhu"
    return render_template("get_insta.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
