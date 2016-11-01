from flask import render_template, request
from app import app
from .forms import ContactForm, SearchContactsForm
from .models import Contact, Subscription
from app import db

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()

    if form.validate_on_submit():
        contact = Contact()
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()

    return render_template('contact-form.html', form=form, submit_label="Add Contact")

@app.route('/search', methods=['GET','POST'])
def search_contacts():
    form = SearchContactsForm()

    results = []

    if form.validate_on_submit():
        contact = Contact.query.filter(Contact.phone_number == form.phone_number.data).first()
        if contact is not None:
            results.append(contact)
    return render_template('search.html', form=form, results=results)

@app.route('/update/<string:phone>', methods=['GET','POST'])
def update_contact(phone):
    form = ContactForm()

    contact = Contact.query.filter(Contact.phone_number == phone).first()

    if request.method == "GET":
        if contact != None:
            form.name.data = contact.name
            form.age.data = contact.age
            form.phone_number.data = contact.phone_number
        else:
            print("Couldn't find {}".format(phone))

    if form.validate_on_submit():
        contact.name = form.name.data
        contact.age = form.age.data

        subs = Subscription.query.filter(Subscription.phone_number == contact.phone_number)
        for sub in subs:
            print("Changed information for: {}. Changed name to {} and age to {}".format(sub.phone_number, contact.name, contact.age))
        db.session.commit()

    return render_template('contact-form.html', form=form, submit_label="Update Contact")

@app.route('/subscribe/<string:phone>', methods=['GET'])
def subscribe(phone):
    if db.session.query(Subscription.phone_number).filter(Subscription.phone_number == phone).scalar() is None:
        sub = Subscription()
        sub.phone_number = phone
        db.session.add(sub)
        db.session.commit()
    return render_template("subscribe.html", phone=phone)
