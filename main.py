from seiver import *
import os
from data import Handler

main_contact = Handler('files/contacts from isaacugochukwu007@gmail.com.txt')
print(repr(main_contact))
filter_files = [file.name for file in os.scandir('files/filters')]
for filters in filter_files:
    filter_ = Handler(f"files/filters/{filters}")
    print(repr(filter_))
    new_contacts = sieve(main_contact.tel_nums, filter_.tel_nums)
    main_contact.tel_nums = new_contacts
    print(repr(main_contact))
contacts = main_contact.rebuild()

vcard = []
for info in contacts:
    card = ["BEGIN:VCARD\n", "VERSION:2.1\n"]
    card += [info_.replace("\n","")+"\n" for info_ in info]
    card.append("END:VCARD\n")  
    vcard.append(card)
    

with open('clean_contacts.vcf', 'w') as file:
    for card in vcard:
        for card_ in card:
            file.write(card_)
