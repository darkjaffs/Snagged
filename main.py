import requests as request
from bs4 import BeautifulSoup
import html
import csv

URL = "https://weworkremotely.com/remote-jobs.rss"

response = request.get(URL)

rawhtml = response.text
decoded_html = html.unescape(rawhtml)

soup = BeautifulSoup(decoded_html, "html.parser")


with open("page.html", "w", encoding="utf-8") as file:
    file.write(decoded_html)


job_items = soup.find_all("item")

with open("jobs.csv","w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Title", "Category", "Link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for job in job_items:
        title = job.find("title").text.strip()
        category = job.find("category").text.strip()
        links = job.find("guid").text.strip()
        writer.writerow({"Title": title, "Category": category, "Link": links})




