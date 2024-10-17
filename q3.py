import re

# validating the format DD/MM/YYYY
date_regex = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$' 

dateinput = input("Enter date: ")
if not re.match(date_regex, dateinput):
    print("Wrong Date Format")