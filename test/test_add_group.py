# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, orm, check_ui, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = orm.get_group_list()
    with allure.step('I add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with added group'):
        new_groups = orm.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            new_groups = list(map(app.group.remove_extra_spaces_in_group_name, new_groups))
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
