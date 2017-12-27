from flask import Flask, render_template, Blueprint,redirect,url_for,request
from list_tweets import list_all_tweets
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for('.get_tweet'))

@app.route("/tweet")
def get_tweet():
    name = "geeksambhu"
    tweet_list= list_all_tweets(name)
    return render_template("tweet_index.html", tweets=tweet_list, name=name)

@app.route('/insta', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'iurl' in request.form:  # basic Flask structure
        url = request.form['iurl']
        raw = requests.get(url)  # make a request to the URL
        soup = BeautifulSoup(raw.text, 'html.parser')  # get the HTML

        links = soup.find(property="og:image")  # find meta with property=og:image
        # "og:video" if you want to download a video

        image = links.get('content')  # get its content
        while image != '':
            return render_template("download.html", image=image)
                # '<img src="' + image + '"' + 'align="center">'  # insert content in img tag

    return render_template('get_insta.html',name="geeksambhu")





if __name__ == "__main__":
    app.run(debug=True)
