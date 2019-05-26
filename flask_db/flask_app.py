from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home_view ():
    if request.method == "GET":
        return render_template("home_view.html", title="Home", type="Sign in")
    if "signup" in request.form:
        return render_template("home_view.html", title="Home", type="Sign up")
    else:
        username = request.form["username"]
        password = request.form["password"]
        db = sqlite3.connect("users_info.db")
        cursor = db.cursor()
        if request.form['submit'] == "Sign in":
            cursor.execute("SELECT user_username FROM users WHERE user_username = ? AND user_password = ?;", [username, password])
            result = cursor.fetchall()
            db.close()
            if len(username) == 0 or len(password) == 0 or len(result) == 0:
                return render_template("home_view.html", title="Home", type="Sign in", fail=True, signup=True)
            return render_template("success.html", username=username, title="Hello")
        else:
            if len(username) == 0 or len(password) == 0:
                return render_template("home_view.html", title="Home", type="Sign Up", invalid=True)
            else:
                cursor.execute("SELECT user_username FROM users WHERE user_username = ?;", [username])
                result = cursor.fetchall()
                if len(result) > 0:
                    return render_template("home_view.html", title="Home", type="Sign up", exists=True)
                cursor.execute("INSERT INTO users (user_username, user_password) VALUES(?, ?);", [username, password])
                db.commit()
                cursor.execute("SELECT * FROM users")
                result = cursor.fetchall()
                db.close()
                print(result)
                return render_template("success.html", username=username, title="Hello")

if __name__ == "__main__":
    app.run(debug=True)
