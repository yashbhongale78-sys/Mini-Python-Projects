import requests
query = input("What type of news do you want to read :")
api = "799640032c5643518f7d358759b89d4d"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-22&sortBy=publishedAt&apiKey={api}"
print(url)

r= requests.get(url)
data = r.json()
articles = data["articles"]

number = 0
for index, article in enumerate(articles):
    print(index+1,".",article["title"], article["url"])
    print("---------------------------------------------------------------")