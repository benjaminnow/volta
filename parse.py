import csv
import pprint
import os
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
ENV = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'templates'))
)


def create_dict():
    data = {}
    with open('data.csv', newline='') as f:
        reader = csv.DictReader(f, fieldnames=['Account','Contact','Title','Activity','Subject','Notes'])
        account = None
        for row in reader:
            # checks if row is the persons name
            if not row['Account'] == 'Account' and not row['Account'] == '' and row['Notes'] == '':
                print(row['Account'])
                # sets account to persons name
                account = row['Account']
                # creates a key in the data dictionary with persons name and a empty list
                # as a value
                data[row['Account']] = []
                # checks if row is not a header row and it is not a blank row
            elif not row['Account'] == 'Account' and not row['Account'] == '':
                # if row not blank or header add to list in persons account
                data[account].append(row)

    # loops through dict and adds keys which don't have any data to a list
    # of to be deleted keys
    keys_to_delete = []
    for k, v in data.items():
        if len(data[k]) == 0:
            keys_to_delete.append(k)

    # loops through list of to be deleted keys and deletes keys from data dict
    for keys in keys_to_delete:
        del data[keys]

    return data


# takes data from dict and sends it to jinja template
def create_template(data):
    template = ENV.get_template('base.html')
    print(template.render(data=data))


#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(create_dict())
#pp.pprint(create_template(create_dict()))
create_template(create_dict())
