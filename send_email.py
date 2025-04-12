from database import get_all_subscribers, get_jobs_by_categories
from email_service import send_email
from app import app

with app.app_context():
    users = get_all_subscribers()

    categories = set(user[1] for user in users)

    category_jobs={}

    for cat in categories:
        category_jobs[cat] = get_jobs_by_categories(cat)
        
    for email, category in users:
        user_jobs = category_jobs.get(category,[])
        if user_jobs:
            send_email(email, user_jobs)
