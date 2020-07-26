from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="James", bday="15", bmonth="October", byear="1992"))
    app.session.logout()