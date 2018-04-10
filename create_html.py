import csv
import pprint
import os
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
ENV = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'templates'))
)

UPLOAD_FOLDER = '/home/ben/programming/volta/uploads/'
CREATED_FOLDER = '/home/ben/programming/volta/templates/created_pages/'

def create_dict(filename):
    data = {}
    with open(UPLOAD_FOLDER + filename, newline='') as f:
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

    # takes data from dictionary created above and puts it into the base template
    template = ENV.get_template('base.html')
    with open(CREATED_FOLDER + filename.split(".")[0] + ".html", 'w') as f:
        f.write(template.render(data=data))

    print(template.render(data=data))
