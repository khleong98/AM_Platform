from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(100), unique=True, nullable=False)
    referrer_id   = db.Column(db.Integer, db.ForeignKey('user.id'))
    point         = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'{self.email} - {self.point}'

class Referral(db.Model):
    __tablename__ = 'referral'

    id            = db.Column(db.Integer, primary_key=True)
    referrer_id   = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    referree_id   = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    referrer      = db.relationship('User', foreign_keys=[referrer_id], backref='referrer')
    referree      = db.relationship('User', foreign_keys=[referree_id], backref='referree')