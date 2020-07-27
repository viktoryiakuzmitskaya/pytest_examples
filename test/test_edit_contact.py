from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Michael", lastname="Scott", mobile="1234567", email="mscott@test.com"))
    app.contact.edit_first_contact(Contact(firstname="James", bday="15", bmonth="October", byear="1992"))
