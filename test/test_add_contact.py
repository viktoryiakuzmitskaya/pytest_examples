# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="John", lastname="Connor", homephone="+45798798798", mobilephone="78897-343-89", workphone="+375(17)676-98-33", secondaryphone="6876876876", email="reer@hkjh.com", email2="3jkj4@fd.by", email3="kjkh-jkj@gmail.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


