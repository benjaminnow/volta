import csv
import pprint

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

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
