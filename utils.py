import re

# This is an email validation regex.
# It matches strings that follow the general pattern of an email address:
# one or more alphanumeric characters, possibly including ".", "_", "%", "+", or "-", 
# followed by an "@" symbol, followed by one or more alphanumeric characters, 
# possibly including ".", "-", followed by a ".", and finally between 2 to 6 alphabetic characters.
e_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z\.]{2,6}$'

# This is a phone number validation regex.
# It matches strings that follow the general pattern of a phone number:
# optionally starts with a "+" and up to 3 digits, possibly separated by spaces or hyphens, 
# followed by three digits (optionally enclosed in parentheses), possibly followed by a space or hyphen, 
# followed by three more digits, possibly followed by a space or hyphen, and finally followed by four digits.
p_regex = r'^(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$'

# This is a strong password validation regex.
# It matches strings that are at least 8 characters long and include at least one lowercase letter, 
# one uppercase letter, one digit, and one special character from the set "@$!%*?&".
s_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def checkvalid(text, regex):
    if re.search(regex, text):
        return False
    else:
        return True
    
if __name__ == '__main__':
    print(("valid", "invalid")[checkvalid('devrel@github.com',e_regex)])
    print(("valid", "invalid")[checkvalid('4255552386',p_regex)])