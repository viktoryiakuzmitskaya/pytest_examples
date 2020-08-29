from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor"))
    # get random contact
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    # check groups where this contact is absent
    available_groups = orm.get_groups_not_containing_contact(contact)
    if not available_groups:
        group = Group(name="TestAddContactGroup")
        app.group.create(group)
    else:
        group = random.choice(available_groups)
    # add contact to group
    app.contact.add_contact_to_group(contact.id, group.id, group.name)
    # check that contact was added
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group
