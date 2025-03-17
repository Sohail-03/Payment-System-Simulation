import sqlite3

def connect_db():
    return sqlite3.connect('payment_system_simulation.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        balance REAL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user INTEGER,
        to_user INTEGER,
        amount REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(from_user) REFERENCES users(id),
        FOREIGN KEY(to_user) REFERENCES users(id)
    )
    ''')
    conn.commit()
    conn.close()

def add_user(name, balance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, balance) VALUES (?, ?)
    ''', (name, balance))
    conn.commit()
    conn.close()

def get_user_balance(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    balance = cursor.fetchone()
    conn.close()
    return balance[0] if balance else None

def update_user_balance(user_id, balance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users SET balance = ? WHERE id = ?
    ''', (balance, user_id))
    conn.commit()
    conn.close()

def record_transaction(from_user, to_user, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transactions (from_user, to_user, amount) VALUES (?, ?, ?)
    ''', (from_user, to_user, amount))
    conn.commit()
    conn.close()
