import requests
from bs4 import BeautifulSoup

url = "https://google.com"
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, 'lxml')
list_of_links = soup.find_all('a')


list_of_external_links = []

for every in list_of_links:
    if "google.com" in every["href"] or "http" not in every["href"]:
        pass
    else:
        list_of_external_links.append(every["href"])

print(list_of_external_links)