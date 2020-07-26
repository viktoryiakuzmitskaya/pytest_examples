from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="group_name_edited"))
    app.session.logout()