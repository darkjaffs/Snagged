import sqlite3

def create_connection():
    """Establish a database connection and return the connection object."""
    return sqlite3.connect("users.db")


def create_tables():
    
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        url TEXT UNIQUE NOT NULL,
        published_date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        category TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()

def insert_jobs(title, category, url, date):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs WHERE url=?", (url,))

    if cursor.fetchone() is None:
        cursor.execute("INSERT into jobs (title, category, url, published_date) VALUES (?,?,?,?)", (title,category,url,date))
        conn.commit()
    
    conn.close()

def insert_users(email,category):

    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT into subscribers (email, category) VALUES (?, ?)", (email, category))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()
        
def get_all_subscribers():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT email, category FROM subscribers")
    users = cursor.fetchall()
    
    conn.close   
    return users

def get_jobs_by_categories(category, limit=10):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
                   SELECT title,url,published_date FROM jobs
                   WHERE category=?
                   ORDER BY published_date DESC
                   LIMIT ?
    
    """, (category, limit))
    
    jobs = cursor.fetchall()
    conn.close()
    return jobs

if __name__ == "__main__":
    create_tables()