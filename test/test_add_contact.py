# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="John", middlename="Robert", lastname="Smith", nickname="Bob", title="Sales manager", company="Some company",
                                   address="New York, 45th Street, 57", home="56789450", mobile="37890406", work="47890593", fax="47589341",
                                   email="jsmith@smth.com", bday="14", bmonth="November", byear="1993"))
    app.session.logout()

