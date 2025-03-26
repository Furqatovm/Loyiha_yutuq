from flask import Flask, redirect, url_for, render_template
import sqlite3
import library


app=Flask(__name__)

def connect_db():
    return sqlite3.connect("library.db")




def add_people(name, emaill, password):
    conn =connect_db()
    cursor =conn.cursor()

    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, emaill, password))
    conn.commit()
    print("user succesfully added")

    cursor.execute("SELECT email FROM users")

    emails =cursor.fetchall()

    for email in emails:
        if email ==emaill:
            print("siz allaqachon registratsiya qilgansiz")




@app.route("/")

def home():
    return render_template("index.html")






if __name__ =="__main__":
    app.run(debug=True)



    






