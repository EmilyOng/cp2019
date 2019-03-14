from flask import *
import sqlite3
# export FLASK_APP=flask_app.py && flask run
app = Flask(__name__)
#decorator
comments=[]
#connection=sqlite3.connect("info.db")
#cursor=connection.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS info (user TEXT,comments TEXT);")
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("main.html",comments=comments)
    comments.append(request.form["contents"])
    #cursor.execute("INSERT INTO info (user,comments) VALUES(?,?)",("USER",request.form["contents"]))
    return redirect(url_for("index"))
