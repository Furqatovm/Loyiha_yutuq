from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
import library


app=Flask(__name__)
app.secret_key ="thisissecretkey"

def connect_db():
    return sqlite3.connect("library.db")


questions =[
{"question": "Who wrote 'Hamlet'?", "option_a": "Shakespeare", "option_b": "Hemingway", "option_c": "Tolstoy", "option_d": "Dostoevsky", "answer": "A"},
{"question": "How old are you?", "option_a": "I'm 20 years old.", "option_b": "I am a teacher.", "option_c": "It is 5 o'clock.", "option_d": "My name is John.", "answer": "A"},
{"question": "Which color is the sky on a clear day?", "option_a": "Red", "option_b": "Green", "option_c": "Blue", "option_d": "Yellow", "answer": "C"},
{"question": "What time does the train leave?", "option_a": "It leaves at 3:00 PM.", "option_b": "It is a car.", "option_c": "She is a teacher.", "option_d": "We eat breakfast.", "answer": "A"},
{"question": "Where do you live?", "option_a": "In a house", "option_b": "By train", "option_c": "In the evening", "option_d": "On the moon", "answer": "A"},
{"question": "Which one is an animal?", "option_a": "Chair", "option_b": "Cat", "option_c": "Book", "option_d": "Table", "answer": "B"},
{"question": "Is she your sister?", "option_a": "Yes, she is.", "option_b": "No, I am.", "option_c": "Yes, I am.", "option_d": "No, he is.", "answer": "A"},
{"question": "What is the opposite of 'hot'?", "option_a": "Cold", "option_b": "Warm", "option_c": "Big", "option_d": "Dry", "answer": "A"},
{"question": "How many days are in a week?", "option_a": "7", "option_b": "5", "option_c": "10", "option_d": "6", "answer": "A"},
{"question": "Which of these is a fruit?", "option_a": "Carrot", "option_b": "Apple", "option_c": "Bread", "option_d": "Chicken", "answer": "B"}
]




@app.route("/quiz", methods =["GET", "POST"])
def quiz():
    user_email =session.get("email")
    if "current_question" not in session:
        session["current_question"] =0
        session["score"] =0
        session["mistakes"] =0

    current_question =session["current_question"]
    if request.method =="POST":
        user_answer =request.form.get("answer")
        correct_answer =questions[current_question]["answer"]

        if user_answer:
            if user_answer == correct_answer:
                session["score"] += 1
            else:
                session["mistakes"] += 1


                # 
        if "next" in request.form and current_question + 1 < len(questions):
            session["current_question"] += 1
        elif "prev" in request.form and current_question > 0:
            session["current_question"] -=1
        elif "submit" in request.form and current_question +1 ==len(questions):
            return redirect(url_for("result"))
        
    return render_template("a1testpage.html", question =questions[current_question], current=current_question, total=len(questions), user_email=user_email)


questions2 =[
{"question": "What is the plural of 'child'?", "option_a": "Childs", "option_b": "Children", "option_c": "Childes", "option_d": "Childrens", "answer": "B"},
    {"question": "Which sentence is correct?", "option_a": "She go to school.", "option_b": "She goes to school.", "option_c": "She going to school.", "option_d": "She gone to school.", "answer": "B"},
    {"question": "Choose the correct preposition: 'I am good ___ English.'", "option_a": "at", "option_b": "on", "option_c": "in", "option_d": "of", "answer": "A"},
    {"question": "What is the past simple of 'go'?", "option_a": "Goed", "option_b": "Gone", "option_c": "Went", "option_d": "Go", "answer": "C"},
    {"question": "Which word is a verb?", "option_a": "Beautiful", "option_b": "Slowly", "option_c": "Run", "option_d": "Happy", "answer": "C"},
    {"question": "Which sentence is in the present continuous tense?", "option_a": "She plays football.", "option_b": "She is playing football.", "option_c": "She played football.", "option_d": "She has played football.", "answer": "B"},
    {"question": "Which sentence is correct?", "option_a": "I can to swim.", "option_b": "I can swimming.", "option_c": "I can swim.", "option_d": "I can swam.", "answer": "C"},
    {"question": "Which word is a noun?", "option_a": "Happy", "option_b": "Run", "option_c": "Cat", "option_d": "Quickly", "answer": "C"},
    {"question": "What is the comparative form of 'fast'?", "option_a": "Faster", "option_b": "More fast", "option_c": "Most fast", "option_d": "Fastest", "answer": "A"},
]


@app.route("/quiz2", methods =["GET", "POST"])
def quiza_2():
    user_email =session.get("email")
    if "current_question2" not in session:
        session["current_question2"] =0
        session["score2"] =0
        session["mistakes2"] =0

    current_question =session["current_question2"]
    if request.method =="POST":
        user_answer =request.form.get("answer")
        correct_answer =questions2[current_question]["answer"]

        if user_answer:
            if user_answer == correct_answer:
                session["score2"] += 1
            else:
                session["mistakes2"] += 1


                # 
        if "next" in request.form and current_question + 1 < len(questions2):
            session["current_question2"] += 1
        elif "prev" in request.form and current_question > 0:
            session["current_question2"] -=1
        elif "submit" in request.form and current_question +1 ==len(questions2):
            return redirect(url_for("resulta2"))
        
    return render_template("a2testpage.html", question =questions2[current_question], current=current_question, total=len(questions2), user_email=user_email)



questions3 =[
  {"question": "What is the comparative form of 'fast'?", "option_a": "Faster", "option_b": "More fast", "option_c": "Most fast", "option_d": "Fastest", "answer": "A"},
  {"question": "Choose the correct past tense of 'go'.", "option_a": "Went", "option_b": "Gone", "option_c": "Goes", "option_d": "Going", "answer": "A"},
  {"question": "Which of these sentences is correct?", "option_a": "She can sings well.", "option_b": "She can sing well.", "option_c": "She can singing well.", "option_d": "She can to sing well.", "answer": "B"},
  {"question": "What is the superlative form of 'big'?", "option_a": "Biggest", "option_b": "More big", "option_c": "Bigger", "option_d": "Most big", "answer": "A"},
  {"question": "Which word is a synonym of 'happy'?", "option_a": "Sad", "option_b": "Angry", "option_c": "Joyful", "option_d": "Bored", "answer": "C"},
  {"question": "Fill in the blank: 'I ___ to the park yesterday.'", "option_a": "Go", "option_b": "Going", "option_c": "Went", "option_d": "Will go", "answer": "C"},
  {"question": "Which of these sentences uses the correct form of 'there'?", "option_a": "Their is a book on the table.", "option_b": "There is a book on the table.", "option_c": "They’re is a book on the table.", "option_d": "There’s a book on the table.", "answer": "B"},
  {"question": "What is the correct question form of 'You like coffee'?", "option_a": "Do you like coffee?", "option_b": "You like coffee?", "option_c": "Do like you coffee?", "option_d": "Like you coffee?", "answer": "A"},
  {"question": "Choose the correct word: 'I have ___ homework to do.'", "option_a": "Much", "option_b": "Many", "option_c": "A lot", "option_d": "Few", "answer": "A"},
  {"question": "Which of these sentences is in the present continuous tense?", "option_a": "I eat lunch now.", "option_b": "I am eating lunch now.", "option_c": "I will eat lunch now.", "option_d": "I ate lunch now.", "answer": "B"}
]


@app.route("/quiz3", methods =["GET", "POST"])
def quiza_3():
    user_email =session.get("email")
    if "current_question3" not in session:
        session["current_question3"] =0
        session["score3"] =0
        session["mistakes3"] =0

    current_question =session["current_question3"]
    if request.method =="POST":
        user_answer =request.form.get("answer")
        correct_answer =questions3[current_question]["answer"]

        if user_answer:
            if user_answer == correct_answer:
                session["score3"] += 1
            else:
                session["mistakes3"] += 1


                # 
        if "next" in request.form and current_question + 1 < len(questions3):
            session["current_question3"] += 1
        elif "prev" in request.form and current_question > 0:
            session["current_question3"] -=1
        elif "submit" in request.form and current_question +1 ==len(questions3):
            return redirect(url_for("resulta3"))
        
        
    return render_template("b1testpage.html", question =questions3[current_question], current=current_question, total=len(questions3), user_email=user_email)



@app.route("/result3")
def resulta3():
    score =session.get("score3", 0)
    mistakes =session.get("mistakes3", 0)

    session.pop("current_question3", None)
    session.pop("score3", None)
    session.pop("mistakes3", None)
    return render_template("resultb1.html", score3=score, mistakes3=mistakes, total=len(questions3))





@app.route("/result")
def result():
    score =session.get("score", 0)
    mistakes =session.get("mistakes", 0)
    session.pop("current_question", None)
    session.pop("score", None)
    session.pop("mistakes", None)
    return render_template("result.html", score=score, mistakes=mistakes, total=len(questions))


@app.route("/result2")
def resulta2():
    score =session.get("score2", 0)
    mistakes =session.get("mistakes2", 0)
    session.pop("current_question2", None)
    session.pop("score2", None)
    session.pop("mistakes2", None)
    return render_template("result2.html", score2=score, mistakes2=mistakes, total=len(questions))



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
    user_email =session.get("email")
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
    return render_template("login.html", user_email =user_email)


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




@app.route("/tests", methods =["POST", "GET"])
def test():
    user_email =session.get("email")
    return render_template("a1test.html", user_email=user_email)




@app.route("/A1-test")
def a1():
    user_email =session.get("email")
    return render_template("index.html", user_email =user_email)

@app.route("/A2-test")
def a2():
    user_email =session.get("email")
    return render_template("a2.html", user_email=user_email)

@app.route("/B1-test")
def b1():
    user_email =session.get("email")
    return render_template("b1.html", user_email=user_email)

@app.route("/B2-test")
def b2():
    user_email =session.get("email")
    return render_template("b2.html", user_email =user_email)

@app.route("/C1-test")
def c1():
    user_email =session.get("email")
    return render_template("c1.html", user_email =user_email)

@app.route("/C2-test")
def c2():
    user_email =session.get("email")
    return render_template("c2.html", user_email=user_email)




if __name__ =="__main__":
    app.run(debug=True)



    






