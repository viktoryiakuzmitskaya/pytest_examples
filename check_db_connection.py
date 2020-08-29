from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    #l = db.get_group_list()
    #l = db.get_groups_containing_contact(Contact(id='451'))
    l = db.get_groups_not_containing_contact(Contact(id='451'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    #db.destroy()
