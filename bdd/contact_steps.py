from pytest_bdd import given, when, then
from model.contact import Contact
from random import randrange
import random


@given('a contact list')
def contact_list(orm):
    return orm.get_contact_list()


@given('a new contact with <firstname>, <lastname>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email1>, <email2>, <email3>')
def new_contact(firstname, lastname, address, homephone, mobilephone, workphone, secondaryphone, email1, email2, email3):
    return Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                   mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, email1=email1,
                   email2=email2, email3=email3)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with added contact')
def verify_contact_added(app, orm, contact_list, new_contact, check_ui):
    old_contacts = contact_list
    new_contacts = orm.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="some name"))
    return orm.get_contact_list()


@given('a random contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the contact list with deleted contact')
def verify_contact_deleted(app, orm, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = orm.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a random contact by index to modify')
def random_contact_by_index(non_empty_contact_list, new_contact):
    old_contacts = non_empty_contact_list
    index = randrange(len(old_contacts))
    contact = new_contact
    contact.id = old_contacts[index].id
    return index, contact


@when('I modify the contact')
def modify_contact(app, random_contact_by_index):
    index, contact = random_contact_by_index
    app.contact.edit_contact_by_id(contact.id, contact)


@then('the new contact list is equal to the contact list with modified contact')
def verify_contact_modified(app, orm, non_empty_contact_list, random_contact_by_index, check_ui):
    index, contact = random_contact_by_index
    old_contacts = non_empty_contact_list
    new_contacts = orm.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
