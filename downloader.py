import requests

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

for item in items:
    print(item['link'])
