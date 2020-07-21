from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="James", middlename="Christian", lastname="Levis", nickname="Chris", title="Regional manager", company="Some company 2",
                                   address="New York, 47th Street, 57", home="56789451", mobile="37890407", work="47890597", fax="47589342",
                                   email="jimlevis@smth.com", bday="15", bmonth="October", byear="1992"))
    app.session.logout()