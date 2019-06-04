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
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_in_group(group)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)