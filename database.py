import sqlite3

def init_db():
    conn = sqlite3.connect('teqra_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, username):
    conn = sqlite3.connect('teqra_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()
