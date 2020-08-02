from model.contact import Contact
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not  None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_option_value(self, field_name, option):
        wd = self.app.wd
        if option is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(option)

    def fill_out_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_option_value("bday", contact.bday)
        self.change_option_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_out_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # check whether delete is available, if not, go to the home page
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        # check whether edit is available, if not, go to the home page
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_out_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[./td]"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            firstname = element.find_elements_by_tag_name("td")[2].text
            lastname = element.find_elements_by_tag_name("td")[1].text
            contacts.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return contacts

