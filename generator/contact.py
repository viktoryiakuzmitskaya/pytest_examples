from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetOptError as err:
    getopt.usage()
    sys.exit(2)

n = 7
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + (string.digits)*20
    #symbols = string.ascii_letters + (string.digits) * 20 + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("fn", 20), lastname=random_string("ln", 20), address=random_string("ad", 50), homephone=random_string("hm", 20),
          mobilephone=random_string("mb", 20), workphone=random_string("wp", 20), secondaryphone=random_string("sp", 20),
            email=random_string("e", 30), email2=random_string("e2", 30), email3=random_string("e3", 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))