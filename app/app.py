from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="user_db"
    )

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return "Login Successful!"
        else:
            return "Invalid Credentials"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
