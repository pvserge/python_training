from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Mod Group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name='11', header='11', footer='11'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Mod Group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name='New Name'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Mod Group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header='New Header'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Mod Group"))
    app.group.edit_first_group(Group(footer='New Footer'))
