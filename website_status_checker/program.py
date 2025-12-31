import requests
import os 
import pandas as pd
import math
data = {
    "Website": [],
    "Status" : [],
    "Status Code": [],
    "Response Time": []
}
try:
    with open('website_status_checker/website_urls.txt', 'r') as file:
        content = file.readlines()
        for url in content:
            url = url.strip()
            try:
                x = requests.get(url, timeout=5)
                print(f"Connection successful. Checking {url} status…")
                response_time = round(x.elapsed.total_seconds(), 2)
                if x.status_code >= 200 and x.status_code <= 299:
                    print(f"✅ Website is working normally (Status: {x.status_code}, Response time: {response_time}s)")
                    data["Website"].append(url)
                    data["Status"].append("Working")
                    data["Status Code"].append(x.status_code)
                    data["Response Time"].append(str(response_time) + "s")
                elif x.status_code >= 300 and x.status_code <=399:
                    print(f"✅ Website is reachable but redirected (Status: {x.status_code})")
                    data["Website"].append(url)
                    data["Status"].append("Working, but redirected to different URL")
                    data["Status Code"].append(x.status_code)
                    data["Response Time"].append(str(response_time) + "s")
                elif x.status_code >= 400 and x.status_code <= 499:
                    print(f"⚠️  Website returned a cleint error (Status: {x.status_code})")
                    data["Website"].append(url)
                    data["Status"].append("Cleint Error")
                    data["Status Code"].append(x.status_code)
                    data["Response Time"].append(str(response_time) + "s")
                elif x.status_code >= 500 and x.status_code <= 599:
                    print(f"❌ Website has a server error (Status: {x.status_code})")
                    data["Website"].append(url)
                    data["Status"].append("Server Error")
                    data["Status Code"].append(x.status_code)
                    data["Response Time"].append(str(response_time) + "s")
            except requests.exceptions.Timeout:
                print("⚠️ Website took too long to respond")
            except requests.exceptions.ConnectionError:
                print("❌ Failed to connect to the website")
            except requests.exceptions.InvalidURL:
                print("❌ Provided URL is invalid")
              
except FileNotFoundError:
    print("File containing URLs not found")                              
df = pd.DataFrame(data)
df.to_csv("website_status_checker\data.csv", index=False)
print("Data Saved to CSV ✅")

# import requests
# import os 
# import pandas as pd
# data = {
#     "Website": [],
#     "Status" : [],
#     "Status Code": [],
#     "Response Time": []
# }
# def checkWebsite(url):
#     try:
#         x = requests.get(url)
#         print(x.status_code)
#     except requests.exceptions.ConnectionError:
#         print("Can not establish connection.")
#     except requests.exceptions.ConnectTimeout:
#         print("Website took too time to respond")
#     except requests.exceptions.InvalidURL:
#         print("Maybe you URL is incorrect")

# try:
#     with open('website_status_checker\website_urls.txt', 'r') as file:
#         urls = file.readlines()
#         for url in urls:
#             checkWebsite(url)
# except FileNotFoundError:
#     print("File cointainig url not found")


    
        








