from model.contact import Contact


def test_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='First Name', lastname='Last Name', address='Addr1',
                                   homephone='+123123123', mobilephone='(222)222222', workphone='111-222-333',
                                   email1='email1@123.123', email2='email2@123.123', email3='email3@123.123',
                                   address2='Addr2', secondaryphone='555555555'))
    contacts_from_db = db.get_contact_list()
    print(sorted(contacts_from_db, key=Contact.id_or_max))
    contacts_from_home_page = app.contact.get_contact_list()
    print(sorted(contacts_from_home_page, key=Contact.id_or_max))
    for contact_from_home_page in contacts_from_home_page:
        for contact_from_db in contacts_from_db:
            if contact_from_home_page.id == contact_from_db.id:
                assert app.contact.clear(contact_from_home_page.firstname) == app.contact.clear(contact_from_db.firstname)
                assert contact_from_home_page.lastname == contact_from_db.lastname
                assert app.contact.clear(contact_from_home_page.address) == app.contact.clear(contact_from_db.address)
                assert app.contact.clear(contact_from_home_page.all_phones_from_home_page) == app.contact.clear(app.contact.merge_phones_like_on_home_page(
                    contact_from_db))
                assert app.contact.clear(contact_from_home_page.all_emails_from_home_page) == app.contact.clear(app.contact.merge_emails_like_on_home_page(
                    contact_from_db))
