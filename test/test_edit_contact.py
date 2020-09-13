from model.contact import Contact
import random
import allure

def test_edit_some_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if db.get_contact_list() == 0:
            app.contact.create(Contact(firstname="John", lastname="Connor"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('Given a contact with new data'):
        new_contact_data = Contact(firstname="Sarah")
    with allure.step('When I enter new contact data'):
        app.contact.edit_contact_by_id(contact.id, new_contact_data)
    with allure.step('Then the new contact list is equal to the old list with modified contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == app.contact.count()
        contact.firstname = new_contact_data.firstname
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)