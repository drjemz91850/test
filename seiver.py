# "that's not how to spell sieve"

import re




def get_tel(info_: list, info_loc: int):
    """returns a dictionary of the telephone number(s) of a contact with the contacts
    location( .index() )  in the main contacts list as key """
    tel_list = []
    for info in reversed(info_):
        if re.search(r"^TEL;", info):
            # print(info)
            num = info.replace("-", "").split(":")[-1].replace("+", "")[:-12:-1][::-1]
            # print(num, info_loc, sep=',')
            tel_list.append(num)
    return {info_loc: tel_list}


def compare(x, y):
    for x_ in x:
        for y_ in y:
            if x_ == y_:
                return True
            else:
                return False


def sieve(phone_book1: dict, phonebook2: dict):
    """phonebook one(1)  should be the main contact list i.e the contacts to be rid of duplicates"""
    found_contacts = {}
    print('Starting PhoneBook New Size:', len(phone_book1))
    # accessing each phone book contact
    for loc, tel_phones in phone_book1.items():
        for loc1, tel_phones1 in phonebook2.items():
            if compare(tel_phones, tel_phones1) is True:
                found_contacts[loc] = tel_phones

    for loc, tel_phones in found_contacts.items():
        phone_book1.pop(loc)
    print('PhoneBook New Size:', len(phone_book1))
    return phone_book1
