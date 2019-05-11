# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='test', lastname='test', middlename='test', nickname='test', title='Mr',
                      company='none', address='Addr1', home='123123123', mobile='123123123', work='123123123',
                      fax='123123123', email='123@123.123', bday='7', bmonth='June', byear='1977', aday='12',
                      amonth='August', ayear='2000', address2='none', phone2='none', notes='none')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
