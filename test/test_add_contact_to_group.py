from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_random_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New Contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New Group"))
    group = random.choice(orm.get_group_list())
    contact = random.choice(orm.get_contact_list())
    old_contacts_in_group = orm.get_contact_in_group(group)
    app.contact.add_to_group(contact, group)
    new_contacts_in_group = orm.get_contact_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
