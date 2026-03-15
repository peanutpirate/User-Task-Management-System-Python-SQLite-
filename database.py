import sqlite3

def connect():
    return sqlite3.connect("app.db")


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_name TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(username):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username) VALUES (?)",(username,))

    conn.commit()
    conn.close()


def add_task(user_id,task):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (user_id, task_name) VALUES (?,?)",
        (user_id,task)
    )

    conn.commit()
    conn.close()


def get_tasks(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT task_name FROM tasks WHERE user_id=?",
        (user_id,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks