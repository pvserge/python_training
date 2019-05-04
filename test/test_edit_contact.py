from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Del Contact"))
    app.contact.edit_first_contact(Contact(firstname='updated test', lastname='updated test', middlename='updated test',
                                           nickname='updated test', title='updated Mr', company='updated none',
                                           address='updated Addr1', home='222222222', mobile='222222222',
                                           work='222222222', fax='222222222', email='222@222.222', bday='2',
                                           bmonth='July', byear='1922', aday='22', amonth='October', ayear='2002',
                                           address2='updated none', phone2='updated none', notes='updated none'))


def test_edit_first_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Del Contact"))
    app.contact.edit_first_contact(Contact(firstname='updated test new'))


def test_edit_first_contact_birth_year(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Del Contact"))
    app.contact.edit_first_contact(Contact(byear='1977'))
