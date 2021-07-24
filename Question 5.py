import string
import random

import numpy as np

source1 = string.ascii_lowercase
source2 = "!#$%&*+_?@^"
source3=string.ascii_uppercase
source1=list(source1)
source2=list(source2)
source3=list(source3)
random.shuffle(source1)
random.shuffle(source2)
random.shuffle(source3)
length=input("please enter the length of he password: ")
length=int(length)
password=[]
x=0
while x<length:

    password.append(source1[0+x])
    x+=1
    if x<length:
        password.append(source2[0+x])
        x+=1
        if x<length:
            password.append(source3[0+x])
            x+=1


print(password)