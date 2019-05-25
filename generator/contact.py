from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + "." + "_"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    digits = string.digits
    prefix = ["", "+111", "(222)", "333-"]
    index = random.randrange(len(prefix))
    return prefix[index] + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


def random_email(maxlen1, maxlen2):
    symbols = string.ascii_letters + string.digits
    prefix = random_string("", maxlen1)
    dmnname = "".join([random.choice(symbols) for i in range(1, maxlen2)])
    zone = "".join([random.choice(symbols) for i in range(1, 3)])
    return "%s@%s.%s" % (prefix, dmnname, zone)


testdata = [
    Contact(firstname=random_string("FirstName", 10), lastname=random_string("LastName", 10),
            address=random_string("Addr1", 20), homephone=random_phone(9), mobilephone=random_phone(9),
            workphone=random_phone(9), secondaryphone=random_phone(9),
            email1=random_email(10, 5), email2=random_email(10, 10), email3=random_email(20, 3))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
