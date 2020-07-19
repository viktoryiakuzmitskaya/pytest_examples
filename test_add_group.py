# -*- coding: utf-8 -*-
import pytest
from group import Group
from application_group import ApplicationGroup


@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group(name="group_name", header="group_header", footer="group_footer"))
    app.logout()
