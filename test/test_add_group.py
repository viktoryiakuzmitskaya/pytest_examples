# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.session.logout()
