import os
import sys
from config import client_id,client_secret
from instagram.client import InstagramAPI

REDIRECT_URL="http://localhost:5000"

def _get_access_token():
    api=InstagramAPI(client_id=client_id, client_secret=client_secret,redirect_uri=REDIRECT_URL)
    redirect_uri=api.get_authorize_login_url(scope="")
    print("visit this page to get access token",redirect_uri)
    code = input("paste in key after redirect: ").strip()
    access_token, user_detail = api.exchange_code_for_access_token(code=code)
    return access_token

def get_insta_post(name):
    access_token = os.environ.get("IG_ACCESS_TOKEN")
    if not access_token:
        _get_access_token()

    api=InstagramAPI(access_token=access_token)
    recent_media, nxt = api.user_recent_media(user_id=name, count = 5)

    for media in recent_media:
        print('thumb_url', media.get_thumbnail_url())

if __name__=="__main__":
    get_insta_post("geeksambhu")