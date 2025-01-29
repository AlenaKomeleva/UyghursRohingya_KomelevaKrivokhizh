# Аль-Биляд
import requests # requests package allows to open websites
from bs4 import BeautifulSoup # package BeautifulSoup works with the context of the web page

# list of saved articles
articles = []
# loop over all found articles
for url in urls:
	# request the website by its address
	response = requests.get(url)
	# search the content
	soup = BeautifulSoup(response.content, 'html.parser')
	# find the content by html key
	html_article = soup.find('div', class_='entry-content')
	# merge all paragraphs into one text
	article_text = html_article.get_text()
	# add the text to the articles list
	articles.append(article_text)

