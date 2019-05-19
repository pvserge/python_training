from model.contact import Contact
from random import randrange


def test_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='First Name', lastname='Last Name', address='Addr1',
                                   homephone='+123123123', mobilephone='(222)222222', workphone='111-222-333',
                                   email1='email1@123.123', email2='email2@123.123', email3='email3@123.123',
                                   address2='Addr2', secondaryphone='555555555'))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_form_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(
        contact_from_edit_page)
