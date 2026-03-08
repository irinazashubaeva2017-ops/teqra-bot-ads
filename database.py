import sqlite3

def init_db():
    # Создаем файл базы данных
    conn = sqlite3.connect('teqra_data.db')
    cursor = conn.cursor()
    # Создаем таблицу пользователей, если её нет
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
    # Добавляем пользователя (ignore — чтобы не было ошибок при повторном входе)
    cursor.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()