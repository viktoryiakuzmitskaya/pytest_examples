from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="TestName"))
    app.group.edit_first_group(Group(name="group_name_edited"))