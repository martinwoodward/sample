import re

regex_a = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

regex_b = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'

def check(myText, regex):

    if(re.fullmatch(regex, myText)):
        print("Valid")
 
    else:
        print("Invalid")

# Driver Code
if __name__ == '__main__' :
    check("", regex_a)
    check("", regex_b)

 