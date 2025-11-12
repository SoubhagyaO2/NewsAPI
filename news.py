import requests 
query = input("What news are you interested in today: ")
api ="6c66a1e21515460c87c340917589bc5d"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-10-08&sortBy=publishedAt&apiKey={api}"

print(url)

r=requests.get(url)
data = r.json()
articles = data["articles"]
for article in articles:
    print(article["title"], article["url"])
    print("\n*******************************\n")
