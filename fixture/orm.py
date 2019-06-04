from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        secondaryphone = Optional(str, column='phone2')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind(provider='mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert_group(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert_group, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert_contact(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname,
                           address=contact.address, homephone=contact.homephone, mobilephone=contact.mobilephone,
                           workphone=contact.workphone, secondaryphone=contact.secondaryphone, email1=contact.email1,
                           email2=contact.email2, email3=contact.email3)
        return list(map(convert_contact, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_group_by_id(self, id):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == id))[0]

    @db_session
    def get_contact_in_group(self, group):
        orm_group = self.get_group_by_id(group.id)
        #return self.convert_contacts_to_model(orm_group.contacts)
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group in c.groups))

    @db_session
    def get_contact_not_in_group(self, group):
        orm_group = self.get_group_by_id(group.id)
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    def destroy(self):
        self.db.disconnect()

