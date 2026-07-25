from datetime import datetime
from database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    ad_soyad = db.Column(db.String(100), nullable=False)
    kullanici_adi = db.Column(db.String(50), unique=True, nullable=False)
    sifre = db.Column(db.String(255), nullable=False)

    rol = db.Column(db.String(20), default="user")
    aktif = db.Column(db.Boolean, default=True)

    son_paylasim = db.Column(db.DateTime, nullable=True)

    olusturma_tarihi = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    baslik = db.Column(db.String(255), nullable=False)

    fiyat = db.Column(db.Integer, nullable=False)

    n11_link = db.Column(db.Text, nullable=False)

    durum = db.Column(
        db.String(20),
        default="Beklemede"
    )

    admin_notu = db.Column(db.Text)

    gonderim_tarihi = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    onay_tarihi = db.Column(db.DateTime)