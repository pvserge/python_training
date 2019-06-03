from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(field_name)).select_by_value(value)

    def fill_contact_form(self, contact, group=None):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)
        if group is not None:
            self.select_field_value("new_group", group.id)

    def create(self, contact):
        wd = self.app.wd
        # open edit page
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("//input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def create_with_group(self, contact, group):
        wd = self.app.wd
        # open edit page
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact, group=group)
        # submit form
        wd.find_element_by_xpath("//input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()

    def delete_contact_by_id(self, contact_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contact_id)
        # deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit updated form
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, contact_id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % contact_id).click()

    def edit_contact_by_id(self, contact_id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(contact_id)
        self.fill_contact_form(contact)
        # submit updated form
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def return_to_home_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name('selected[]').get_attribute('value')
                last_name = element.find_element_by_xpath(".//td[2]").text
                first_name = element.find_element_by_xpath(".//td[3]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                address = element.find_element_by_xpath(".//td[4]").text
                self.contact_cache.append(Contact(lastname=last_name, firstname=first_name, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def get_contact_info_form_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute('value')
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        homephone = wd.find_element_by_name("home").get_attribute('value')
        workphone = wd.find_element_by_name("work").get_attribute('value')
        mobilephone = wd.find_element_by_name("mobile").get_attribute('value')
        secondaryphone = wd.find_element_by_name("phone2").get_attribute('value')
        email1 = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        address = wd.find_element_by_name("address").get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, email1=email1, email2=email2, email3=email3,
                       address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email1, contact.email2, contact.email3]))))

    def remove_extra_spaces(self, s):
        return re.sub(" +", " ", s).strip(" ")

    def remove_extra_spaces_in_contact_names(self, contact):
        if contact.firstname is not None:
            contact.firstname = self.remove_extra_spaces(contact.firstname)
        if contact.lastname is not None:
            contact.lastname = self.remove_extra_spaces(contact.lastname)
        if contact.middlename is not None:
            contact.middlename = self.remove_extra_spaces(contact.middlename)
        return contact

