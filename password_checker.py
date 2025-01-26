def main():
    password=(input("enter password(at least 8 characters): "))
    n=len(password)
    if n<8:
        print("needed at least 8 characters")
    else:
        a,b,c,d=False,False,False,False
        for x in password:
            if x.isupper(): 
                a=True
            elif x.islower():
                b=True
            elif x.isdigit():
                c=True
            elif not x.isalnum():
                d=True
        if a and b and c and d:
            print("strong password")
        else:
            print("weak password")
main()    