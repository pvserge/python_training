from model.contact import Contact
from model.group import Group
import random


def test_delete_random_contact_from_random_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New Group"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_in_group(group)) == 0:
        app.contact.create_with_group(Contact(firstname="New Contact"), group=group)
    old_contacts = orm.get_contact_in_group(group)
    print(len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_in_group(group)
    print(len(new_contacts))
    print(new_contacts)
    old_contacts.remove(contact)
    print(len(old_contacts))
    print(old_contacts)
    assert old_contacts == new_contacts