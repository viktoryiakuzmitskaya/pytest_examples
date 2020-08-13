from model.contact import Contact
from random import randrange

def test_address_on_home_page_for_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor", address=("%s, %s %s" % ("Los Angeles", str(randrange(1000)), "Nickel Road")), workphone="w44654532", email="hgjhg@.mnk.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address
