from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list')
def group_list(orm):
    return orm.get_group_list()


@given('a new group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with added group')
def verify_group_edit(app, orm, group_list, new_group, check_ui):
    old_groups = group_list
    new_groups = orm.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = list(map(app.group.remove_extra_spaces_in_group_name, new_groups))
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="some name"))
    return orm.get_group_list()


@given('a random group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old list with deleted group')
def verify_group_deleted(app, orm, non_empty_group_list, random_group, check_ui):
    old_groups = non_empty_group_list
    new_groups = orm.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        new_groups = list(map(app.group.remove_extra_spaces_in_group_name, new_groups))
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
