import json
from bs4 import BeautifulSoup
import requests

def search_articles(pattern, page, iterator):
    i = 0
    url = 'https://www.blogdumoderateur.com/page/' + page + '?s=' + pattern

    response_bdm = requests.get(url)
    soup_bdb = BeautifulSoup(response_bdm.text, features="lxml")
    if response_bdm.status_code != 200:
        raise Exception('Erreur lors de la requête : {}'.format(response_bdm.status_code))

    article_dict = {}
    articles = soup_bdb.find_all('article')

    if response_bdm.status_code == 200:
        while i < iterator:
            page = str(int(page) + 1)
            url = 'https://www.blogdumoderateur.com/page/' + page + '?s=' + pattern
            if requests.get(url).status_code == 200:
                response_bdm = requests.get(url)
                #  add the response to the soup without replace the existing soup
                soup_bdb = BeautifulSoup(response_bdm.text, 'html.parser')
                articles += soup_bdb.find_all('article')
            else: 
                print('No more pages')
                break

    for article in articles:
        id = article.get('id')

        title = article.find('h3').text.replace('\xa0', ' ')            # Title
        
        try:image = article.find('img')['src']                # Image
        except:image = None
       
        try:link = article.find('a')["href"]                            # Link
        except:link = article.parent['href']

        try:theme = article.find('span', 'favtag').text                 # Catégorie
        except:theme = article.find_previous('h2').text
        
        date = article.find('time')['datetime'].split('T')[0]           # Date
        
        article_dict[id] = { 'title' :title, 'date'  :date, 'link':link, 'image' :image, 'categorie' : theme }

    # with open ('searchResult.json', 'w') as f:json.dump(article_dict, f)
    return article_dict