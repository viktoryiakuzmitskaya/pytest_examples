from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db, orm):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact.id, group.id, group.name)
    contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    assert contact in contacts_in_group
