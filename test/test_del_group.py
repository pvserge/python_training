from model.group import Group
import random


def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Del Group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        new_groups = list(map(app.group.remove_extra_spaces_in_group_name, new_groups))
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
