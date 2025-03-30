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

if __name__ == "__main__":
    create_tables()