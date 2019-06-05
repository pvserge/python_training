from model.contact import Contact
import random


def test_delete_random_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Del Contact"))
    old_contacts = orm.get_contact_list()
    print("Amount of contact before deletion: %s" % len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    print("Amount of contact after deletion: %s" % len(new_contacts))
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
