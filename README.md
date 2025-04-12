# Job Scraper and Notification System

This is a web application that scrapes job listings from various sources, categorizes them, and sends customized job notifications via email to users based on their preferences.

## Features

- **Job Scraping:** The app scrapes job listings from multiple sources, including RSS feeds.
- **Job Categorization:** Jobs are categorized based on user preferences (e.g., Backend, Frontend, Marketing, etc.).
- **Email Notifications:** Users receive curated job listings via email based on their selected category.
- **User Subscription:** Users can subscribe with their email and category preferences through a simple web form.

## Technologies Used

- **Backend:**
  - **Flask:** Web framework used to build the backend of the application.
  - **Flask-Mail:** Library for handling email notifications.
  - **BeautifulSoup:** Used for parsing and scraping job listings from RSS feeds.

- **Frontend:**
  - **HTML/CSS:** Simple frontend for user interaction, where users can subscribe with their email and category preference.
  
## Setup and Installation

### Requirements

- Python 3.x
- Pip (Python package installer)
- A valid email provider (e.g., Gmail, SendGrid) for sending emails

