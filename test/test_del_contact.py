from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Michael", lastname="Scott", mobile="1234567", email="mscott@test.com"))
    app.contact.delete_first_contact()