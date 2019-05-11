from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Mod Group"))
    old_groups = app.group.get_group_list()
    group = Group(name='11', header='11', footer='11')
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Mod Group"))
#    old_groups = app.group.get_group_list()
#    group = Group(name='New Name')
#    group.id = old_groups[0].id
#    app.group.edit_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Mod Group"))
#    old_groups = app.group.get_group_list()
#    group = Group(header='New Header')
#    group.id = old_groups[0].id
#    group.name = old_groups[0].name
#    app.group.edit_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_footer(app):
#    if app.group.count() == 0:
#       app.group.create(Group(name="Mod Group"))
#    old_groups = app.group.get_group_list()
#    group = Group(footer='New Footer')
#    group.id = old_groups[0].id
#    group.name = old_groups[0].name
#    app.group.edit_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
