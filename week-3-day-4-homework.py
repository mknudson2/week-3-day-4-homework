"""
Instructions: 
You have a text file named user_records.txt which contains information about users in the following format:

FirstName LastName, Age, Country

Your task is to use Python and regular expressions (regex) to extract and print the age and country of each user.

For example, if you have a line that reads "John Doe, 25, United States", your script should print "Age: 25, Country: United States".

Some lines might be improperly formatted and do not contain all the required information. If a line doesn't conform to the required format, your script should print "Invalid record".

Use “with open()’ to open the file and ‘readlines()’ to read all the lines.

Make use of regex groups in your pattern. The ‘re.compile()’ function will be helpful.

Your output should look something like this:

Age: 25, Country: United States
Age: 30, Country: Canada
Invalid record
Age: 45, Country: United Kingdom
Invalid record

Create a function that takes in the file name and the regex pattern as arguments and prints out the results.
Add a count for the number of valid and invalid records.
"""
#looking for 4 total outputs

import re

with open('./user_records.txt') as f:
    data = f.readlines()

user_info = re.compile(r'([A-Z][a-z]+ [A-Z][a-z]+), ([0-9]{1,3}), ([A-Za-z][A-Za-z ]*)$')

def extracted_info(user_records, user_info):
    valid_records = 0
    invalid_records = 0
    
    print('\n')
    print('='*25)
    print('       User Data')
    print('='*25)
    for line in user_records:
        match = re.match(user_info, line)
        if match:
            age = match.group(2)
            country = match.group(3)
            print(f'Age: {age}, Country: {country}')
            valid_records += 1
        else:
            print("Invalid Record")
            invalid_records += 1
    print(f"\n Valid Records Count: {valid_records}")
    print(f" Invalid Records Count: {invalid_records}\n")
    
print(extracted_info(data, user_info))
