import requests as request
from bs4 import BeautifulSoup
import html
import csv
from datetime import datetime
from database import insert_jobs

rss_feeds = {
    "Customer Support": "https://weworkremotely.com/categories/remote-customer-support-jobs.rss",
    "Product Jobs": "https://weworkremotely.com/categories/remote-product-jobs.rss",
    "Full-Stack Programming": "https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss",
    "Back-End Programming": "https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss",
    "Front-End Programming": "https://weworkremotely.com/categories/remote-front-end-programming-jobs.rss",
    "All Programming": "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "Sales and Marketing": "https://weworkremotely.com/categories/remote-sales-and-marketing-jobs.rss",
    "Management and Finance": "https://weworkremotely.com/categories/remote-management-and-finance-jobs.rss",
    "Design": "https://weworkremotely.com/categories/remote-design-jobs.rss",
    "Devops and System Admin": "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
    "Others": "https://weworkremotely.com/categories/all-other-remote-jobs.rss"
}

category = "Full-Stack Programming"

URL = rss_feeds[category]

response = request.get(URL)

rawhtml = response.text
decoded_html = html.unescape(rawhtml)

soup = BeautifulSoup(decoded_html, "xml")

with open("page.html", "w", encoding="utf-8") as file:
    file.write(decoded_html)


job_items = soup.find_all("item")

for job in job_items:
        title = job.find("title").text.strip()
        category = job.find("category").text.strip()
        url = job.find("guid").text.strip()
        date_str = job.find("pubDate").text.strip()
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")  
        date = dt.strftime("%d %b %Y") 
        insert_jobs(title, category, url, date)


with open("jobs.csv","w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Title", "Category", "Link", "Date Published"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for job in job_items:
        title = job.find("title").text.strip()
        category = job.find("category").text.strip()
        links = job.find("guid").text.strip()
        date_str = job.find("pubDate").text.strip()
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")  
        date = dt.strftime("%d %b %Y") 
        writer.writerow({"Title": title, "Category": category, "Link": links, "Date Published": date})




