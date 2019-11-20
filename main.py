#! /usr/bin/env python3

import sys
from mypackage.birthdays import return_birthday

if len(sys.argv) == 3:			
    first_name = str(sys.argv[1])
    last_name = str(sys.argv[2])
    user_input = first_name + ' ' + last_name
else:
    print("Enter a valid name")
    exit()


return_birthday(user_input)

