import re

e_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z\.]{2,6}$'
p_regex = r'^(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$'
s_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def checkvalid(text, regex):
    if re.search(regex, text):
        return False
    else:
        return True
    
if __name__ == '__main__':
    print(("valid", "invalid")[checkvalid('devrel@github.com',e_regex)])
    print(("valid", "invalid")[checkvalid('4255552386',p_regex)])