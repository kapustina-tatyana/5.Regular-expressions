import re
from pprint import pprint
import csv

tel_pattern = r"(\+7|8)\s*\(?(\d{3})\)?[\s-]*\(?(\d{3})\)?[\s-]*\(?(\d{2})\)?\s*[\s-]*\(?(\d{2})\)?(\s)*\(?(доб*\.*)\)?\s*\(?(\d{4})*\)?"

format_pattern = r"+7(\2)\3-\4-\5\6\7\8"


with open("phonebook_raw.csv", encoding = "UTF-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pprint(contacts_list)


def phone_number_formater():
  clean_list = []
  for contacts_str in contacts_list:
    full_name = ' '.join(contacts_str[:3]).split(' ')
    result = re.sub(tel_pattern, format_pattern, contacts_str[5])
    res_list = [ full_name[0], full_name[1], full_name[2], contacts_str[3], contacts_str[4], result, contacts_str[6]]
    clean_list.append(res_list)


  return clean_list

def duplicate_remove(contacts: list):
  for contact in contacts:
    last_first_name = contact[0] + contact[1]
    for new_contact in contacts:
      new_last_first_name = new_contact[0] + new_contact[1]
      if last_first_name == new_last_first_name:
        if contact[0] == "": contact[0] = new_contact[0]
        if contact[1] == "": contact[1] = new_contact[1]
        if contact[2] == "": contact[2] = new_contact[2]
        if contact[3] == "": contact[3] = new_contact[3]
        if contact[4] == "": contact[4] = new_contact[4]
        if contact[5] == "": contact[5] = new_contact[5]
        if contact[6] == "": contact[6] = new_contact[6]


      result_list = list()
      for i in contacts:
        if i not in result_list:
          result_list.append(i)

  return result_list


if __name__ == "__main__":
  contacts_list = duplicate_remove(phone_number_formater())

  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)