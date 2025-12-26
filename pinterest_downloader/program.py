import requests
from bs4 import BeautifulSoup
import os

os.makedirs("images", exist_ok=True)

with open("urls.txt", "r") as file:
    pins = file.readlines()

headers = {
    "User-Agent": "Mozilla/5.0"
}

for index, pin_url in enumerate(pins):
    pin_url = pin_url.strip()
    print(f"Downloading from: {pin_url}")

    response = requests.get(pin_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    image_tag = soup.find("meta", property="og:image")

    if image_tag:
        image_url = image_tag["content"]

        img_data = requests.get(image_url).content

        with open(f"images/image_{index+1}.jpg", "wb") as img:
            img.write(img_data)

        print("✔ Image downloaded\n")
    else:
        print("❌ Image not found\n")
