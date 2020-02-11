Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> someInt = float(input("roll times: "))
print("You entered : " + str(someInt))
print(f"You entered : {someInt}")

import random
roll = random.randint(1,6)


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

i=0
while(i < someInt):
    roll = random.randint(1,6)
    print (roll)
    i+= 1


    if (someInt == 1):
        one+=1
        print(one)
    elif(someInt == 2):
        two+=1
        print(two)
    elif(someInt == 3):
        three+=1
        print(three)
    elif(someInt == 4):
        four+=1
        print(four)
    elif(someInt == 5):
        five+=1
        print(five)
    elif(someInt == 6):
        six+= 1
        print(six)
       
print(one/someInt)
print(two/someInt)
print(three/someInt)
print(four/someInt)
print(five/someInt)
print(six/someInt)
