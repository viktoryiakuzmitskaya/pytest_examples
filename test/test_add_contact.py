# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + (string.digits)*20 + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("fn", 20), lastname=random_string("ln", 20), address=random_string("ad", 100), homephone=random_string("hm", 20),
          mobilephone=random_string("mb", 20), workphone=random_string("wp", 20), secondaryphone=random_string("sp", 20),
            email=random_string("e", 30), email2=random_string("e2", 30), email3=random_string("e3", 30))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


