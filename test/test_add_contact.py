# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, orm, check_ui, json_contacts):
    contact = json_contacts
    old_contacts = orm.get_contact_list()
    app.contact.create(contact)
    new_contacts = orm.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

