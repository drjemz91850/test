import re


def organize(lines: list):
    """receives output of file.readlines() which is a list
    and returns a dictionary of ordered vcf contacts """
    contacts_list = []
    # creates store for each vcf card
    unhandled = []
    contact = []
    opened = False
    for line in lines:
        if re.search(r"^BEGIN:", line):
            contact = []
            opened = True
        elif re.search(r"^END:", line) and opened:
            v, *info = contact
            contacts_list.append(info)
            opened = False
        elif opened:
            contact.append(line)
        else:
            unhandled.append((line, lines.index(line) + 1))

    return {"contacts": contacts_list, "unhandled_lines": unhandled}
