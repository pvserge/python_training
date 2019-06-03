from model.group import Group
import random


def test_edit_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Mod Group"))
    old_groups = db.get_group_list()
    new_group = Group(name='11', header='11', footer='11')
    group_to_mod = random.choice(old_groups)
    id_to_mod = group_to_mod.id
    app.group.edit_group_by_id(id_to_mod, new_group)
    new_groups = db.get_group_list()
    for group in old_groups:
        if group.id == id_to_mod:
            group.name = new_group.name
            group.footer = new_group.footer
            group.header = new_group.header
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = list(map(app.group.remove_extra_spaces_in_group_name, new_groups))
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

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
