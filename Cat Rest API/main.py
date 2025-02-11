import os
import requests
from bs4 import BeautifulSoup
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def GetCatPics():
    cat_url_lst = []
    URL = "https://icanhas.cheezburger.com/cats"

    # Add a User-Agent to avoid being blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)

    if page.status_code != 200:
        return f"Error: Unable to fetch page (Status Code {page.status_code})"

    soup = BeautifulSoup(page.content, "html.parser")
    
    # Find all divs containing images
    cat_containers = soup.find_all("div", class_="resp-media-wrap")

    for cat_image in cat_containers:
        img_tag = cat_image.find("img")  # Find the <img> tag inside the div
        
        if img_tag:
            # Check for lazy-loaded images
            cat_url = img_tag.get("data-src") or img_tag.get("data-original") or img_tag.get("src")
            
            # Ensure the URL isn't a base64 placeholder
            if cat_url and not cat_url.startswith("data:image"):
                cat_url_lst.append(cat_url)

    if not cat_url_lst:
        return "No cat images found!"
    selected_cat = random.choice(cat_url_lst)
    return f"""
    <html>
    <head>
        <title>Random Cat</title>
    </head>
    <body style="text-align: center; margin-top: 50px;">
        <h1>Here's a Random Cat (hopefully) 🐱</h1>
        <img src="{selected_cat}" alt="Random Cat" style="max-width: 80%; height: auto; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);">
        <br><br>
        <a href="/">🔄 Get Another Cat</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
