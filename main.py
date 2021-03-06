from bs4 import BeautifulSoup
import requests

# https://www.immobilienscout24.de/robots.txt "robots.txt" für Infos zum scrapen anhängen.

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes = [int(score.split()[0]) for score in article_upvotes]

largest = max(article_upvotes)
largest_index = article_upvotes.index(largest)

