import sqlite3


conn =sqlite3.connect("library.db")

cursor =conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL   
)""")

conn.commit()



cursor.execute("""
    INSERT INTO users (email, password) VALUES ("muhammadyusuffurqatov91@gmail.com", "muhammadyusuf")
""")

conn.commit()
conn.close()








