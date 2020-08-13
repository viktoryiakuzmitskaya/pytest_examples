from model.contact import Contact
import re
from random import randrange

def test_emails_on_home_page_for_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor", workphone="w44654532", email="hgjhg@.mnk.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))