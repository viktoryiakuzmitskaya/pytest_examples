from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, email=None, nickname=None, title=None, company=None, address=None,
                       fax=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.fax = fax
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
