from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>, <address> and <homephone>', target_fixture="new_contact")
def new_contact(firstname, lastname, address, homephone):
    return Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with added contact')
def verify_group_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("test name"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_group_deleted(app, db, check_ui, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@given('a contact with new data', target_fixture="edited_contact_data")
def edited_contact_data():
    return Contact(firstname="edited_firstname")


@when('I enter new contact data')
def edit_contact(app, random_contact, edited_contact_data):
    app.contact.edit_contact_by_id(random_contact.id, edited_contact_data)


@then('the new contact list is equal to the old list with modified contact')
def verify_contact_deleted(app, db, check_ui, non_empty_contact_list, random_contact, edited_contact_data):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    random_contact.firstname = edited_contact_data.firstname
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)