from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from models import User, Post

print("APP DOSYASI ÇALIŞTI")

app = Flask(__name__)

app.secret_key = "fiyatpaylas_v1"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fiyatpaylas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def create_admin():
    admin = User.query.filter_by(kullanici_adi="admin").first()

    if not admin:
        admin = User(
            ad_soyad="Yönetici",
            kullanici_adi="admin",
            sifre=generate_password_hash("123456"),
            rol="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin hesabı oluşturuldu.")


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(
            kullanici_adi=username
        ).first()

        if user:

            if check_password_hash(user.sifre, password):

                if user.rol == "admin":
                    return redirect("/admin")

                return "Kullanıcı Paneli"

        flash("Kullanıcı adı veya şifre hatalı.")

    return render_template("login.html")


@app.route("/admin")
def admin_panel():
    return render_template("admin.html")


@app.route("/test")
def test():
    return "<h1>TEST SAYFASI</h1>"


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        create_admin()

    app.run(debug=True)