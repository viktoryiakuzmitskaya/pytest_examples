from sys import maxsize

class Contact:

    def __init__(self, id=None, firstname=None,  lastname=None, address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None, email=None, email2=None, email3=None, all_emails_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        #self.middlename = middlename
        #self.nickname = nickname
        #self.title = title
        #self.company = company
        #self.fax = fax
        #self.bday = bday
        #self.bmonth = bmonth
        #self.byear = byear

    def __repr__(self):
        return "%s:%s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s" % (self.id, self.firstname, self.lastname, self.address,
        self.homephone, self.mobilephone, self.workphone, self.secondaryphone, self.email, self.email2, self.email3, self.all_phones_from_home_page, self.all_emails_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname and self.address == other.address and self.all_phones_from_home_page == other.all_phones_from_home_page and \
               self.all_emails_from_home_page == other.all_emails_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
