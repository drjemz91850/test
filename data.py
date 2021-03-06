from handler import organize
from seiver import *


class Handler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.contact = self.get_file()['contacts']
        self.unhandled = self.get_file()["unhandled_lines"]
        self.tel_nums = {}
        self.contact_names = {}
        self.tel()
        self.contact_name()

    def get_file(self):
        with open(self.file_name, 'r') as file:
            det = file.readlines()
            result_dict = organize(det)
        return result_dict

    def tel(self):
        for contact in self.contact:
            phone = get_tel(contact, self.contact.index(contact))
            self.tel_nums.update(phone)

    def contact_name(self):
        for contact in self.contact:
            name = get_names(contact, self.contact.index(contact))
            self.contact_names.update(name)

    def rebuild(self, data: dict):
        contacts = []
        for loc, _ in data:
            try:
                contacts.append(self.contact[loc])
            except IndexError as error:
                print(error, "Error during rebuild", sep="\t")
                continue
        vcard = []
        for info in contacts:
            card = ["BEGIN:VCARD\n", "VERSION:2.1\n"]
            card += [info_.replace("\n", "") + "\n" for info_ in info]
            card.append("END:VCARD\n")
            vcard.append(card)

        return vcard

    def __repr__(self):
        rep = f'Contact Created from: {self.file_name} \n Contact List Size: {len(self.contact)}\n' \
              f'Unhandled Contacts Size: {len(self.unhandled)}\n' \
              f'Tel_Nums: {len(self.tel_nums)}\n' \
              f'Contact_Names{len(self.contact_names)}'
        return rep

    def vcard_filer(self, filename: str, contact_list: rebuild, mode: str = "w"):
        """filename: filename or path to new/old file"""
        with open(filename, mode) as file:
            for card in contact_list:
                for card_ in card:
                    file.write(card_)


