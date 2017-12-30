import mimetypes
import requests
from bs4 import BeautifulSoup
import json

while True:
    try:
        url = input("Your Website:")
        website = requests.get(url)
        break
    except:
        print("I can't open the website!")
        break
html = BeautifulSoup(website.text, "html.parser")
scripts = html.find_all("script")
count=0
for script in enumerate(scripts):

    if count<2:
        count += 1
        continue

    print (script)
    images = json.loads((str(script[1])[52:]).text)
    if images["entry_data"]["ProfilePage"]["user"]["media"]["thumbnail_resources"]["src"]:
        print(images["entry_data"]["ProfilePage"]["user"]["media"]["thumbnail_resources"]["src"])

# images=json.loads(html.find('script', type='application/ld+json').text)
# print (images["entry_data"]["ProfilePage"]["user"]["media"]["thumbnail_resources"]["src"])


# def download(url, filename):
#     file_url = requests.get(url)
#     file_extension = mimetypes.guess_extension(file_url.headers['content-type'])
#     with open(filename+file_extension, 'wb') as file:
#         file.write(file_url.content)
#
# for index, image in enumerate(images):
#     download(image["src"], "image{index}".format(index=index))