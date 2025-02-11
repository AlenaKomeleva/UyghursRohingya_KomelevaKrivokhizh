import requests
from bs4 import BeautifulSoup

articles = []
for url in urls:
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	html_article = soup.find('div', class_='row-article-body')
	article_text = html_article.get_text()
	articles.append(article_text)
