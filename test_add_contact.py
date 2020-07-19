# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login("admin", "secret")
        app.create_contact(Contact(firstname="John", middlename="Robert", lastname="Smith", nickname="Bob", title="Sales manager", company="Some company",
                            address="New York, 45th Street, 57", home="56789450", mobile="37890406", work="47890593", fax="47589341",
                            email="jsmith@smth.com", bday="14", bmonth="November", byear="1993"))
        app.logout()

