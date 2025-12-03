import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/todos"

try:
    r = requests.get(url, timeout=10)
    print("Status:", r.status_code)
    if r.ok:
        data = r.json()
        df = pd.DataFrame(data)
        print(df.head())
    else:
        print("Not OK")
        print("Body:", r.text[:200])  # peek at response
except Exception as e:
    print("Error:", e)
