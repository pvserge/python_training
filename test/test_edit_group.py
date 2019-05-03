from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name='11', header='11', footer='11'))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name='New Name'))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header='New Header'))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer='New Footer'))
