from model.contact import Contact
from model.group import Group
import random

def test_remove_contact_from_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor"))
    # get random contact
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    # check groups containing this contact
    available_groups = orm.get_groups_containing_contact(contact)
    if not available_groups:
        groups = orm.get_group_list()
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact.id, group.id, group.name)
    else:
        group = random.choice(available_groups)
    # remove contact from group
    app.contact.remove_contact_from_group(group.id, contact.id)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group
