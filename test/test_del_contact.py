from model.contact import Contact
import random
import allure


def test_delete_random_contact(app, orm, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(orm.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="Del Contact"))
        old_contacts = orm.get_contact_list()
    with allure.step('Given a random contact'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete a contact %s from the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the contact list with deleted contact'):
        new_contacts = orm.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
