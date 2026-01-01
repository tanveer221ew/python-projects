import requests
import pandas as pd
import os
data = {
    "Website name": [],
    "Status code": [],
    "Response time":[],
    "Status":[]
}
def checkWebsite():
    try:
        def update_data():
            data["Website name"].append(url)
            data["Response time"].append(str(response_time)+"s")
            data["Status code"].append(status_code)
            data["Status"].append(status)
        x = requests.get(url, timeout=5)
        status_code = x.status_code
        response_time = round(x.elapsed.total_seconds(), 2)
        if 200 <= status_code <= 299:
            status = "Working"
            print(f"🟢 {url} is working Normaly (Status Code: {status_code}, Response Time: {response_time}s)")
            update_data()
        elif 300 <= status_code <= 399:
            status = "Redirected"
            print(f"🟢 {url} is redirected to different URL (Status Code: {status_code}, Response Time: {response_time}s)")
            update_data()
        elif 400 <= status_code <= 499:
            status = "Cleint Error"
            f"🟢 {url} Returned a cleint error (Status Code: {status_code}, Response Time: {response_time}s)"
            update_data()
        elif 500 <= status_code <= 599:
            status = "Server Error"
            f"🟢 {url} Returned a server error (Status Code: {status_code}, Response Time: {response_time}s)"
            update_data()
    except requests.exceptions.ConnectionError:
        response_time = None
        status_code = None
        status = "Connection Error"
        print("⛔ Failed to estabish connection with website")
        update_data()
    except requests.exceptions.Timeout:
        status = "Timeout"
        response_time = None
        status_code = None
        print("🔴 Website took too long to respond")
        update_data()
    except requests.exceptions.InvalidURL:
        status = "Invalid Error"
        response_time = None
        status_code = None
        print("❗ Maybe your url is incorrect")
        update_data()


try:
    print("🔍 Starting to check websites")
    with open("urls.txt", 'r') as file:
        content = file.readlines()
        for url in content:
            url = url.replace("\n", "")
            if not url.startswith("https://"):
                url = "http://" + url
            checkWebsite()
except FileNotFoundError:
    print("❌ File containing website URLs not found")
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
print(df)
print("Data saved to Excel File")