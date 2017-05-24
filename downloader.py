import requests
import os

from config import API_KEY, CX

query = input("Enter image query.\n")
max_results = int(input("How many images to download?\n"))
# imgsize = input("Image size?\n")
# filetype = input("File type?\n")

endpoint = 'https://www.googleapis.com/customsearch/v1'
search_type = 'image'

payload = {'key': API_KEY, 'q': query, 'num': max_results, 'cx': CX, 'searchType': search_type}
r = requests.get(endpoint, params=payload)

items = r.json()['items']

for i, item in enumerate(items, start=1):
    filename = item['link'].split('/')[-1]

    if not os.path.isdir("./img/{}".format(query)):
        os.mkdir("./img/{}".format(query))

    filepath = "./img/{}/{}".format(query, filename)

    img_file = requests.get(item['link'], stream=True)
    with open(filepath, 'wb') as f:
        for chunk in img_file.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
