from handler import organize
from seiver import get_tel


class Handler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.contact = self.get_file()['contacts']
        self.unhandled = self.get_file()["unhandled_lines"]
        self.tel_nums = {}
        self.tel()

    def get_file(self):
        with open(self.file_name, 'r') as file:
            det = file.readlines()
            result_dict = organize(det)
        return result_dict

    def tel(self):
        for contact in self.contact:
            phone = get_tel(contact, self.contact.index(contact))
            self.tel_nums.update(phone)

    def rebuild(self):
        updated_contacts = []
        for loc, _  in self.tel_nums.items():
            updated_contacts.append(self.contact[loc])
        print(len(updated_contacts))
        return updated_contacts

    def __repr__(self):
        rep = f'Contact Created from: {self.file_name} \n Contact List Size: {len(self.contact)}\n' \
              f'Unhandled Contacts Size: {len(self.unhandled)}\n' \
              f'Tel_Nums: {len(self.tel_nums)}'
        return rep
