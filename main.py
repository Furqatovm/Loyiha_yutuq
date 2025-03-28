from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
import library


app=Flask(__name__)
app.secret_key ="thisissecretkey"

def connect_db():
    return sqlite3.connect("library.db")




def add_people(emaill, password):
    conn =connect_db()
    cursor =conn.cursor()

    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (emaill, password))
    conn.commit()
    print("user succesfully added")

    cursor.execute("SELECT email FROM users")

    emails =cursor.fetchall()

    for email in emails:
        if email ==emaill:
            print("siz allaqachon registratsiya qilgansiz")




@app.route("/")

def home():
    user_email =session.get("email")
    return render_template("index.html", user_email=user_email)







@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method =="POST":
        email =request.form["email"]
        password =request.form["password"]

        conn =connect_db()
        cursor =conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ? AND password =?", (email, password))
        user =cursor.fetchone()

        conn.close()

        if user:
            session["email"] =user[1]
            return redirect(url_for("home"))
        else:
            return "Xatolik yuz berid"
    return render_template("login.html")


@app.route("/signup", methods =["POST", "GET"])
def signup():
    if request.method =="POST":
        email =request.form["email"]
        password =request.form["password"]

        conn =connect_db()
        cursor =conn.cursor()

        cursor.execute("SELECT * FROM users where email = ?", (email,))

        existing_user =cursor.fetchone()

        if existing_user:
            return "Bu allaqachon ro'yhatdan o'tgan"
        
        
        cursor.execute("INSERT INTO users(email, password) VALUES (?, ?)", (email, password))

        conn.commit()
        conn.close()

        return redirect(url_for("login"))
    
    return render_template("register.html")



@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("home"))



if __name__ =="__main__":
    app.run(debug=True)



    






