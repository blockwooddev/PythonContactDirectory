from app import db

class Contact(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    age = db.Column(db.Integer)
    phone_number = db.Column(db.String(20), primary_key=True)


class Subscription(db.Model):
    phone_number = db.Column(db.String(20), db.ForeignKey(Contact.phone_number), primary_key=True)
    contact = db.relationship("Contact", backref="subscription", foreign_keys=phone_number)
