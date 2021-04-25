def is_integer(s):
    state=0
    for i in s:
        if state==0:
            if(i=="-"):
                state=2
            elif(i>="0" and i<="9"):
                state=1
            else:
                state=3
        elif state==1:
            if(i>="0" and i<="9"):
                state=1
            else:
                state=3
        elif state==2:
            if(i>="0" and i<="9"):
                state=1
            else:
                state=3
        elif state==3:
            return False
    if state==1:
        return True
    else:
        return False

def main():
    while True:
        getnum = True
        while getnum == True:
            num=(input("Enter a number: "))
            intcheck = is_integer(num)
            if intcheck == False:
                print("Not a positive integer")
            elif intcheck == True:
                num = int(num)
                if num < 0:
                    print("Not a positive integer")
                else:
                    getnum = False
        
        if num%4 != 0:
            print(num, "is not a leap year.")
        else:
            if num%100 == 0:
                if num%400 == 0:
                    print(num, "is a leap year.")
                else:
                    print(num, "is not a leap year.")
            else:
                print(num, "is a leap year.")

        getnum = True
        while getnum == True:
            new=(input("Would you like to check another number? (0: No / 1: Yes): "))
            intcheck = is_integer(new)
            if intcheck == True:
                new = int(new)
                if new == 1 or new == 0:
                    getnum = False

        if new == 0:
            print("Goodbye")
            break
main()