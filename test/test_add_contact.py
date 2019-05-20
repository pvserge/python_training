# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    digits = string.digits
    prefix = ["", "+111", "(222)", "333-"]
    index = random.randrange(len(prefix))
    return prefix[index] + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


def random_email(maxlen1, maxlen2):
    symbols = string.ascii_letters + string.digits
    prefix = random_string("", maxlen1)
    dmnname = "".join([random.choice(symbols) for i in range(random.randrange(maxlen2))])
    zone = "".join([random.choice(symbols) for i in range(3)])
    return "%s@%s.%s" % (prefix, dmnname, zone)


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="",
                    secondaryphone="", email1="", email2="", email3="")] + [
    Contact(firstname=random_string("FirstName", 10), lastname=random_string("LastName", 10), address=random_string("Addr1", 20),
            homephone=random_phone(9), mobilephone=random_phone(9),
            workphone=random_phone(9), secondaryphone=random_phone(9),
            email1=random_email(10, 5), email2=random_email(10, 10), email3=random_email(20, 3))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
