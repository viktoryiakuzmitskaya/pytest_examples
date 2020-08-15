from model.contact import Contact
import re
from random import randrange

def test_contact_data_for_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor", address=("%s, %s %s" % ("Los Angeles", str(randrange(1000)), "Nickel Road")), workphone="w44654532", email="hgjhg@.mnk.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #compare firstname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    #compare lastname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    #compare address
    assert contact_from_home_page.address == contact_from_edit_page.address
    #compare phones
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    #compare emails
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

