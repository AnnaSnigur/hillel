import os


def exec_query(query):
    import sqlite3
    print(os.path.join(os.getcwd(), 'chinook.db'))
    conn = sqlite3.connect("./chinook.db")
    cur = conn.cursor()
    cur.execute(query)
    record = cur.fetchall()
    return record
