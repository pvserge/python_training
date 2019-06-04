from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_random_group(app, orm, check_ui, json_contacts):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New Group"))
    group = random.choice(orm.get_group_list())
    contact = json_contacts
    old_contacts_in_group = orm.get_contact_in_group(group)
    app.contact.create_with_group(contact, group=group)
    new_contacts_in_group = orm.get_contact_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
