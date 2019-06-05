from model.contact import Contact
from model.group import Group
import random


def test_delete_random_contact_from_random_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New Contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New Group"))
    group = random.choice(orm.get_group_list())
    contact = random.choice(orm.get_contact_list())
    if len(orm.get_contact_in_group(group)) == 0:
        app.contact.add_to_group(contact, group)
    old_contacts_in_group = orm.get_contact_in_group(group)
    contact_to_delete = random.choice(old_contacts_in_group)
    app.contact.remove_contact_from_group(contact_to_delete, group)
    new_contacts_in_group = orm.get_contact_in_group(group)
    old_contacts_in_group.remove(contact_to_delete)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)