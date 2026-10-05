import requests

query = input("What type of news are you interested in today? ")
api = "7011954f94644a62926b822b5e8127e3"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-09-05&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n***************************\n")