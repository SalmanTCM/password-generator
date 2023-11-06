import string
import random

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = int (input("Enter password length \n"))
    passcount = int (input( "Enter How many Password do you want \n" ))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    with open('password.txt', 'w') as f:
        for i in range (0,passcount):
            random.shuffle(s)
            # print(s)
            pas = ("".join(s[0:passlen]))
            print(pas)
            f.writelines(list(pas))
            f.write("\n")

gen()