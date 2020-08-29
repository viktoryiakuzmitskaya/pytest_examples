from model.contact import Contact
from model.group import Group
import random

def test_remove_contact_from_group(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.remove_contact_from_group(group.id, group.name, contact.id)
    #contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    #assert contact in contacts_in_group
