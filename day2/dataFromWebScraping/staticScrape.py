import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

res = requests.get(url, timeout=10)
soup = BeautifulSoup(res.text, "html.parser")

quotes = [q.get_text(strip=True) for q in soup.select("span.text")]
authors = [a.get_text(strip=True) for a in soup.select("small.author")]

for q, a in zip(quotes, authors):
    print(f"{q}  — {a}")
