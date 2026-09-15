import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")

first_title_span = soup.find("span", class_="titleline")

first_article_link = first_title_span.find("a")

first_article_text = first_article_link.text

first_article_upvotes = soup.find(id="score_49700477", class_="score").text

title_spans = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for title_span in title_spans:
    article = title_span.find("a")
    article_texts.append(article.get_text())
    article_links.append(article.get("href"))

print(article_texts)