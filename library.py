import sqlite3


conn =sqlite3.connect("library.db")

cursor =conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL   
)""")

conn.commit()



# cursor.execute("""
#     INSERT INTO users (name, email, password) VALUES ("Muhammadyusuf", "muhammadyusuffurqatov91@gmail.com", "muhammadyusuf")
# """)








