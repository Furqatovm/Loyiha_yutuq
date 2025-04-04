from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3, os
import library


app=Flask(__name__)
app.secret_key ="thisissecretkey"

def connect_db():
    return sqlite3.connect("library.db")


questions = [
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

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    user_email = session.get("email")
    session.setdefault("current_question", 0)
    session.setdefault("score", 0)
    session.setdefault("mistakes", 0)
    session.setdefault("answers", [])  # Foydalanuvchi javoblarini saqlash uchun

    current_question = session["current_question"]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions[current_question]["answer"]

        # Foydalanuvchi javobini tekshirish
        if user_answer:
            # Javobni saqlash (faqat agar bu javob hali saqlanmagan bo'lsa)
            if len(session["answers"]) <= current_question:
                session["answers"].append(user_answer)
            else:
                session["answers"][current_question] = user_answer

            # Javobni tekshirish va hisoblash
            if user_answer == correct_answer:
                session["score"] += 1
            else:
                session["mistakes"] += 1

        # "next" tugmasi bosilsa
        if "next" in request.form and current_question + 1 < len(questions):
            session["current_question"] += 1

        # "prev" tugmasi bosilsa
        elif "prev" in request.form and current_question > 0:
            session["current_question"] -= 1
            # Orqaga qaytishda javoblarni qayta hisoblashni to'xtatish (xatoliklarni hisoblamaslik)
            prev_answer = session["answers"][current_question - 1]  # Oldingi savolning javobini olish
            prev_correct_answer = questions2[current_question - 1]["answer"]  # Oldingi savolning to'g'ri javobini olish

            if prev_answer == prev_correct_answer:
                session["score"] -= 1
            else:
                session["mistakes"] -= 1

        elif "submit" in request.form and current_question + 1 == len(questions):
            return redirect(url_for("result"))

        session.modified = True  # Session yangilanishi uchun

        return redirect(url_for("quiz"))  # F5 bosganda savol takrorlanmasligi uchun

    return render_template("a1testpage.html", question=questions[current_question], current=current_question, total=len(questions), user_email=user_email)


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
    {"question": "Which sentence is in the past perfect tense?", "option_a": "She eats lunch.", "option_b": "She ate lunch.", "option_c": "She had eaten lunch.", "option_d": "She is eating lunch.", "answer": "C"}
]

@app.route("/quiz2", methods=["GET", "POST"])
def quiz2():
    user_email = session.get("email")
    session.setdefault("current_question2", 0)
    session.setdefault("score2", 0)
    session.setdefault("mistakes2", 0)
    session.setdefault("answers", [])  # Foydalanuvchi javoblarini saqlash uchun

    current_question = session["current_question2"]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions2[current_question]["answer"]

        # Foydalanuvchi javobini tekshirish
        if user_answer:
            # Javobni saqlash (faqat agar bu javob hali saqlanmagan bo'lsa)
            if len(session["answers"]) <= current_question:
                session["answers"].append(user_answer)
            else:
                session["answers"][current_question] = user_answer

            # Javobni tekshirish va hisoblash
            if user_answer == correct_answer:
                session["score2"] += 1
            else:
                session["mistakes2"] += 1

        # "next" tugmasi bosilsa
        if "next" in request.form and current_question + 1 < len(questions2):
            session["current_question2"] += 1

        # "prev" tugmasi bosilsa
        elif "prev" in request.form and current_question > 0:
            session["current_question2"] -= 1
            # Orqaga qaytishda javoblarni qayta hisoblashni to'xtatish (xatoliklarni hisoblamaslik)
            prev_answer = session["answers"][current_question - 1]  # Oldingi savolning javobini olish
            prev_correct_answer = questions2[current_question - 1]["answer"]  # Oldingi savolning to'g'ri javobini olish

            if prev_answer == prev_correct_answer:
                session["score2"] -= 1
            else:
                session["mistakes2"] -= 1

        elif "submit" in request.form and current_question + 1 == len(questions2):
            return redirect(url_for("resulta2"))

        session.modified = True  # Session yangilanishi uchun

        return redirect(url_for("quiz2"))  # F5 bosganda savol takrorlanmasligi uchun

    return render_template("a2testpage.html", question=questions2[current_question], current=current_question, total=len(questions2), user_email=user_email)




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


@app.route("/quiz3", methods=["GET", "POST"])
def quiz3():
    user_email = session.get("email")
    session.setdefault("current_question3", 0)
    session.setdefault("score3", 0)
    session.setdefault("mistakes3", 0)
    session.setdefault("answers", [])  # Foydalanuvchi javoblarini saqlash uchun

    current_question = session["current_question3"]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions3[current_question]["answer"]

        # Foydalanuvchi javobini tekshirish
        if user_answer:
            # Javobni saqlash (faqat agar bu javob hali saqlanmagan bo'lsa)
            if len(session["answers"]) <= current_question:
                session["answers"].append(user_answer)
            else:
                session["answers"][current_question] = user_answer

            # Javobni tekshirish va hisoblash
            if user_answer == correct_answer:
                session["score3"] += 1
            else:
                session["mistakes3"] += 1

        # "next" tugmasi bosilsa
        if "next" in request.form and current_question + 1 < len(questions3):
            session["current_question3"] += 1

        # "prev" tugmasi bosilsa
        elif "prev" in request.form and current_question > 0:
            session["current_question3"] -= 1
            # Orqaga qaytishda javoblarni qayta hisoblashni to'xtatish (xatoliklarni hisoblamaslik)
            prev_answer = session["answers"][current_question - 1]  # Oldingi savolning javobini olish
            prev_correct_answer = questions3[current_question - 1]["answer"]  # Oldingi savolning to'g'ri javobini olish

            if prev_answer == prev_correct_answer:
                session["score3"] -= 1
            else:
                session["mistakes3"] -= 1

        elif "submit" in request.form and current_question + 1 == len(questions3):
            return redirect(url_for("resulta3"))

        session.modified = True  # Session yangilanishi uchun

        return redirect(url_for("quiz3"))  # F5 bosganda savol takrorlanmasligi uchun

    return render_template("b1testpage.html", question=questions3[current_question], current=current_question, total=len(questions3), user_email=user_email)







@app.route("/result3")
def resulta3():
    score =session.get("score3", 0)
    mistakes =session.get("mistakes3", 0)

    session.pop("current_question3", None)
    session.pop("score3", None)
    session.pop("mistakes3", None)
    return render_template("resultb1.html", score3=score, mistakes3=mistakes, total=len(questions3))


questions4 = [
    {"question": "Which sentence is in the passive voice?", "option_a": "She writes a letter.", "option_b": "A letter is written by her.", "option_c": "She is writing a letter.", "option_d": "She wrote a letter.", "answer": "B"},
    {"question": "Choose the correct past participle of 'take'.", "option_a": "Took", "option_b": "Taking", "option_c": "Taken", "option_d": "Takes", "answer": "C"},
    {"question": "Which of these sentences is in the future perfect tense?", "option_a": "I will finish the report tomorrow.", "option_b": "I will have finished the report by tomorrow.", "option_c": "I finish the report tomorrow.", "option_d": "I am finishing the report tomorrow.", "answer": "B"},
    {"question": "What is the correct form of the adjective in this sentence: 'He is ___ than I am.'", "option_a": "More tall", "option_b": "Tallest", "option_c": "Taller", "option_d": "Most tall", "answer": "C"},
    {"question": "Which of these sentences uses the correct word order?", "option_a": "She never goes to the gym.", "option_b": "Never she goes to the gym.", "option_c": "She goes never to the gym.", "option_d": "Gym she never goes to.", "answer": "A"},
    {"question": "Which sentence uses the correct form of 'be'?", "option_a": "I am being tired.", "option_b": "I am tired.", "option_c": "I being tired.", "option_d": "I tired am.", "answer": "B"},
    {"question": "Which word is a synonym for 'significant'?", "option_a": "Unimportant", "option_b": "Meaningful", "option_c": "Small", "option_d": "Unknown", "answer": "B"},
    {"question": "Fill in the blank: 'I ___ never been to Paris.'", "option_a": "Have", "option_b": "Had", "option_c": "Has", "option_d": "Am", "answer": "A"},
    {"question": "What is the correct form of the verb in this sentence: 'If I ___ you, I would study harder.'", "option_a": "Am", "option_b": "Was", "option_c": "Were", "option_d": "Be", "answer": "C"},
    {"question": "Which of these sentences is in the third conditional?", "option_a": "If I study, I will pass the exam.", "option_b": "If I studied, I would pass the exam.", "option_c": "If I had studied, I would have passed the exam.", "option_d": "If I study, I pass the exam.", "answer": "C"}
]



@app.route("/quiz4", methods=["GET", "POST"])
def quiz4():
    user_email = session.get("email")
    session.setdefault("current_question4", 0)
    session.setdefault("score4", 0)
    session.setdefault("mistakes4", 0)
    session.setdefault("answers", [])  # Foydalanuvchi javoblarini saqlash uchun

    current_question = session["current_question4"]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions4[current_question]["answer"]

        # Foydalanuvchi javobini tekshirish
        if user_answer:
            # Javobni saqlash (faqat agar bu javob hali saqlanmagan bo'lsa)
            if len(session["answers"]) <= current_question:
                session["answers"].append(user_answer)
            else:
                session["answers"][current_question] = user_answer

            # Javobni tekshirish va hisoblash
            if user_answer == correct_answer:
                session["score4"] += 1
            else:
                session["mistakes4"] += 1

        # "next" tugmasi bosilsa
        if "next" in request.form and current_question + 1 < len(questions4):
            session["current_question4"] += 1

        # "prev" tugmasi bosilsa
        elif "prev" in request.form and current_question > 0:
            session["current_question4"] -= 1
            # Orqaga qaytishda javoblarni qayta hisoblashni to'xtatish (xatoliklarni hisoblamaslik)
            prev_answer = session["answers"][current_question - 1]  # Oldingi savolning javobini olish
            prev_correct_answer = questions4[current_question - 1]["answer"]  # Oldingi savolning to'g'ri javobini olish

            if prev_answer == prev_correct_answer:
                session["score4"] -= 1
            else:
                session["mistakes4"] -= 1

        elif "submit" in request.form and current_question + 1 == len(questions4):
            return redirect(url_for("resulta4"))

        session.modified = True  # Session yangilanishi uchun

        return redirect(url_for("quiz4"))  # F5 bosganda savol takrorlanmasligi uchun

    return render_template("b2testpage.html", question=questions4[current_question], current=current_question, total=len(questions4), user_email=user_email)




@app.route("/result4")
def resulta4():
    score =session.get("score4", 0)
    mistakes =session.get("mistakes4", 0)

    session.pop("current_question4", None)
    session.pop("score4", None)
    session.pop("mistakes4", None)
    return render_template("resultb2.html", score4=score, mistakes4=mistakes, total=len(questions4))


questions5 = [
    {"question": "Which sentence is in the passive voice?", "option_a": "She will have completed the task.", "option_b": "The task has been completed by her.", "option_c": "She completed the task.", "option_d": "She has been completing the task.", "answer": "B"},
    {"question": "Identify the correct past participle of 'forbid'.", "option_a": "Forbid", "option_b": "Forbids", "option_c": "Forbidden", "option_d": "Forbade", "answer": "C"},
    {"question": "Which of the following sentences is in the future perfect continuous tense?", "option_a": "By next year, I will have been working here for a decade.", "option_b": "By next year, I will have worked here for a decade.", "option_c": "By next year, I will work here for a decade.", "option_d": "By next year, I will be working here for a decade.", "answer": "A"},
    {"question": "Choose the correct form of the adjective in this sentence: 'She is by far ___ student in the class.'", "option_a": "The most intelligent", "option_b": "More intelligent", "option_c": "Most intelligent", "option_d": "The intelligentest", "answer": "A"},
    {"question": "Which sentence correctly uses inversion?", "option_a": "Never before have I seen such dedication.", "option_b": "I have never before seen such dedication.", "option_c": "Never before I seen such dedication.", "option_d": "Never I have seen before such dedication.", "answer": "A"},
    {"question": "Which of these sentences contains a reduced relative clause?", "option_a": "The book that was written by her is fascinating.", "option_b": "The book, which was written by her, is fascinating.", "option_c": "The book written by her is fascinating.", "option_d": "She wrote a fascinating book.", "answer": "C"},
    {"question": "Which word is the best synonym for 'ephemeral'?", "option_a": "Eternal", "option_b": "Short-lived", "option_c": "Confusing", "option_d": "Profound", "answer": "B"},
    {"question": "Fill in the blank: 'Had he known about the meeting, he ___ there on time.'", "option_a": "Will have been", "option_b": "Would have been", "option_c": "Was", "option_d": "Would be", "answer": "B"},
    {"question": "Which of these is an example of a mixed conditional?", "option_a": "If I had studied harder, I would pass the test.", "option_b": "If I study hard, I will pass the test.", "option_c": "If I had studied harder, I would have passed the test.", "option_d": "If I study hard, I pass the test.", "answer": "A"},
    {"question": "Which sentence correctly expresses an unreal past situation?", "option_a": "If he tried harder, he will succeed.", "option_b": "If he had tried harder, he would have succeeded.", "option_c": "If he tries harder, he will succeed.", "option_d": "If he tries harder, he would succeed.", "answer": "B"}
]


@app.route("/quiz5", methods=["GET", "POST"])
def quiz5():
    user_email = session.get("email")
    session.setdefault("current_question5", 0)
    session.setdefault("score5", 0)
    session.setdefault("mistakes5", 0)
    session.setdefault("answers", [])  # Foydalanuvchi javoblarini saqlash uchun

    current_question = session["current_question5"]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions5[current_question]["answer"]

        # Foydalanuvchi javobini tekshirish
        if user_answer:
            # Javobni saqlash (faqat agar bu javob hali saqlanmagan bo'lsa)
            if len(session["answers"]) <= current_question:
                session["answers"].append(user_answer)
            else:
                session["answers"][current_question] = user_answer

            # Javobni tekshirish va hisoblash
            if user_answer == correct_answer:
                session["score5"] += 1
            else:
                session["mistakes5"] += 1

        # "next" tugmasi bosilsa
        if "next" in request.form and current_question + 1 < len(questions5):
            session["current_question5"] += 1

        # "prev" tugmasi bosilsa
        elif "prev" in request.form and current_question > 0:
            session["current_question5"] -= 1
            # Orqaga qaytishda javoblarni qayta hisoblashni to'xtatish (xatoliklarni hisoblamaslik)
            prev_answer = session["answers"][current_question - 1]  # Oldingi savolning javobini olish
            prev_correct_answer = questions5[current_question - 1]["answer"]  # Oldingi savolning to'g'ri javobini olish

            if prev_answer == prev_correct_answer:
                session["score5"] -= 1
            else:
                session["mistakes5"] -= 1

        elif "submit" in request.form and current_question + 1 == len(questions5):
            return redirect(url_for("resulta5"))

        session.modified = True  # Session yangilanishi uchun

        return redirect(url_for("quiz5"))  # F5 bosganda savol takrorlanmasligi uchun

    return render_template("c1testpage.html", question=questions5[current_question], current=current_question, total=len(questions5), user_email=user_email)



@app.route("/result5")
def resulta5():
    score =session.get("score5", 0)
    mistakes =session.get("mistakes5", 0)

    session.pop("current_question5", None)
    session.pop("score5", None)
    session.pop("mistakes5", None)
    return render_template("resultc1.html", score5=score, mistakes5=mistakes, total=len(questions5))



questions6 = [
    {"question": "Which sentence demonstrates the correct use of a past subjunctive structure?", "option_a": "If he tries harder, he will succeed.", "option_b": "If he were to try harder, he might succeed.", "option_c": "If he had tried harder, he would have succeeded.", "option_d": "If he tries harder, he would succeed.", "answer": "C"},
    {"question": "Identify the correctly used past perfect continuous tense sentence.", "option_a": "By the time we arrived, they had been waiting for two hours.", "option_b": "By the time we arrived, they have been waiting for two hours.", "option_c": "By the time we arrived, they were waiting for two hours.", "option_d": "By the time we arrived, they waited for two hours.", "answer": "A"},
    {"question": "Which of these sentences contains an advanced cleft structure?", "option_a": "What I find fascinating is her ability to learn languages.", "option_b": "She has an ability to learn languages.", "option_c": "Her ability to learn languages is fascinating.", "option_d": "It is fascinating to see her learn languages.", "answer": "A"},
    {"question": "Choose the correct transformation using nominalization: 'The manager explained the policy clearly.'", "option_a": "The manager gave a clear explanation of the policy.", "option_b": "The manager clearly explained the policy.", "option_c": "The manager explained the policy in a clear way.", "option_d": "The policy was clearly explained by the manager.", "answer": "A"},
    {"question": "Which sentence exemplifies a reduced adverbial clause?", "option_a": "While he was watching TV, he heard a noise.", "option_b": "Watching TV, he heard a noise.", "option_c": "He was watching TV when he heard a noise.", "option_d": "He heard a noise while watching TV.", "answer": "B"},
    {"question": "Which of these sentences uses a correct advanced modal verb structure?", "option_a": "She must have forgotten her keys at home.", "option_b": "She must forgot her keys at home.", "option_c": "She must has forgotten her keys at home.", "option_d": "She must be forgot her keys at home.", "answer": "A"},
    {"question": "Identify the correct sentence demonstrating ellipsis.", "option_a": "I wanted to buy the book, but they didn't have any.", "option_b": "I wanted to buy the book, but they didn’t have it.", "option_c": "I wanted to buy the book, but they said it was out of stock.", "option_d": "I wanted to buy the book, but I couldn't find one.", "answer": "A"},
    {"question": "Which sentence contains a correct example of a compound-complex structure?", "option_a": "Although it was late, we continued working, and we finally finished the project.", "option_b": "It was late, so we stopped working.", "option_c": "Although it was late, we stopped working.", "option_d": "It was late; therefore, we stopped working.", "answer": "A"},
    {"question": "Which of the following uses an emphatic structure correctly?", "option_a": "It is John who won the competition.", "option_b": "John, he won the competition.", "option_c": "John was the winner of the competition.", "option_d": "John, who won the competition, is my friend.", "answer": "A"},
    {"question": "Which of the following is an example of a sentence using inversion after negative adverbials?", "option_a": "Seldom have I seen such commitment.", "option_b": "I have seldom seen such commitment.", "option_c": "Seldom I have seen such commitment.", "option_d": "I seen such commitment seldom.", "answer": "A"}
]



@app.route("/quiz6", methods=["GET", "POST"])
def quiz6():
    user_email = session.get("email")
    session.setdefault("current_question6", 0)
    session.setdefault("score6", 0)
    session.setdefault("mistakes6", 0)
    session.setdefault("answers", [])  # Foydalanuvchi javoblarini saqlash uchun

    current_question = session["current_question6"]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions6[current_question]["answer"]

        # Foydalanuvchi javobini tekshirish
        if user_answer:
            # Javobni saqlash (faqat agar bu javob hali saqlanmagan bo'lsa)
            if len(session["answers"]) <= current_question:
                session["answers"].append(user_answer)
            else:
                session["answers"][current_question] = user_answer

            # Javobni tekshirish va hisoblash
            if user_answer == correct_answer:
                session["score6"] += 1
            else:
                session["mistakes6"] += 1

        # "next" tugmasi bosilsa
        if "next" in request.form and current_question + 1 < len(questions6):
            session["current_question6"] += 1

        # "prev" tugmasi bosilsa
        elif "prev" in request.form and current_question > 0:
            session["current_question6"] -= 1
            # Orqaga qaytishda javoblarni qayta hisoblashni to'xtatish (xatoliklarni hisoblamaslik)
            prev_answer = session["answers"][current_question - 1]  # Oldingi savolning javobini olish
            prev_correct_answer = questions6[current_question - 1]["answer"]  # Oldingi savolning to'g'ri javobini olish

            if prev_answer == prev_correct_answer:
                session["score6"] -= 1
            else:
                session["mistakes6"] -= 1

        elif "submit" in request.form and current_question + 1 == len(questions6):
            return redirect(url_for("resulta6"))

        session.modified = True  # Session yangilanishi uchun

        return redirect(url_for("quiz6"))  # F5 bosganda savol takrorlanmasligi uchun

    return render_template("c2testpage.html", question=questions6[current_question], current=current_question, total=len(questions6), user_email=user_email)




@app.route("/result6")
def resulta6():
    score =session.get("score6", 0)
    mistakes =session.get("mistakes6", 0)

    session.pop("current_question6", None)
    session.pop("score6", None)
    session.pop("mistakes6", None)
    return render_template("resultc2.html", score6=score, mistakes6=mistakes, total=len(questions6))






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
    return render_template("result2.html", score2=score, mistakes2=mistakes, total=len(questions2))



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
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)), debug=True)



    






