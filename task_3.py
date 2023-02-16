import requests
from bs4 import BeautifulSoup as bs
 
URL = 'https://greenatom.ru/'

def tag_parser(url):
    data = requests.get(URL, headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
    soup = bs(data.content, 'lxml')

    all_tags = soup.find_all()
    tags_with_attrs = [tag.attrs for tag in all_tags if tag.attrs]

    return 'All tags: {0}, tags with attrs: {1}.'.format(len(all_tags), len(tags_with_attrs))

#print(tag_parser(URL))