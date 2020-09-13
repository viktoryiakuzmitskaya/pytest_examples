from model.contact import Contact
import random
import allure

def test_delete_some_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if db.get_contact_list() == 0:
            app.contact.create(Contact(firstname="John", lastname="Connor"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact %s to the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == app.contact.count()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)