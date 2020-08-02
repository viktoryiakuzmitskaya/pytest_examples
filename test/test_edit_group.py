from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="TestName"))
    app.group.edit_first_group(Group(name="group_name_edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)