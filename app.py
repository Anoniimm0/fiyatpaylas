from flask import Flask, render_template, request

print("APP DOSYASI ÇALIŞTI")

from database import db
from models import User, Post

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fiyatpaylas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def login():

    print("İstek geldi:", request.method)

    if request.method == "POST":
        print("POST ÇALIŞTI")

        username = request.form.get("username")
        password = request.form.get("password")

        print("Kullanıcı:", username)
        print("Şifre:", password)

    return render_template("login.html")


@app.route("/test")
def test():
    return "<h1>TEST SAYFASI</h1>"


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)