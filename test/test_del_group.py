from model.group import Group
import random
import allure


def test_delete_random_group(app, orm, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="Del Group"))
        old_groups = orm.get_group_list()
    with allure.step('Given a random group'):
        group = random.choice(old_groups)
    with allure.step('I delete a group %s from the list' % group):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list with deleted group'):
        new_groups = orm.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            new_groups = list(map(app.group.remove_extra_spaces_in_group_name, new_groups))
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
