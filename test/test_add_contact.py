# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(is_phone, prefix, maxlen):
    if is_phone:
        symbols = string.ascii_letters + (string.digits)*50 + string.punctuation + " "*10
    else:
        symbols = (string.ascii_letters)*50 + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, lastname=lastname, address=address,
            homephone=homephone, mobilephone=mobilephone, workphone=workphone,
            secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)
    for firstname in ["", random_string(False, "fn", 20)]
    for lastname in ["", random_string(False, "ln", 20)]
    for address in ["", random_string(False, "adr", 100)]
    for homephone in ["", random_string(True, "hm", 20)]
    for mobilephone in ["", random_string(True, "mb", 20)]
    for workphone in ["", random_string(True, "wp", 20)]
    for secondaryphone in ["", random_string(True, "sp", 20)]
    for email in ["", random_string(False, "e", 30)]
    for email2 in ["", random_string(False, "e2", 30)]
    for email3 in ["", random_string(False, "e3", 30)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


