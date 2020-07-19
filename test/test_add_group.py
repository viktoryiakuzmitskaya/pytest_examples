# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import ApplicationGroup


@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.session.logout()
