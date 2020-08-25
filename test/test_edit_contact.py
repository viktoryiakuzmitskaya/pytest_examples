from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(firstname="Sarah")
    app.contact.edit_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    contact.firstname = new_contact_data.firstname
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)