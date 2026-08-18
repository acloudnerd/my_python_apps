from datetime import datetime, timedelta
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "JZGIG9A3YFNNR5LY"
}

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()
time_series = data["Time Series (Daily)"]
data_list = [value for (key, value) in time_series.items()]
yesterday_closing = float(data_list[0]['4. close'])

day_before_yesterday = float(data_list[1]['4. close'])
diff = abs(yesterday_closing - day_before_yesterday)

percentage = (diff / day_before_yesterday) * 100

if percentage > 1:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": "fa7167f4050e4b22848c84a2e1940e82"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()

    articles = news_data["articles"][:3]

    the_three_headlines = [{"headline": article["title"], "brief": article["description"]} for article in articles]
    print(the_three_headlines)

# did not implement the twillio part

