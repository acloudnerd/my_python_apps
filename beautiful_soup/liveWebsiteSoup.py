import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")

first_title_span = soup.find("span", class_="titleline")

first_article_link = first_title_span.find("a")

print(first_article_link.text)