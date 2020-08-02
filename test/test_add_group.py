# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

