def main():
    amt=int(input("enter total bill amount: "))
    n=int(input("enter no of people: "))
    t=int(input("any tip percentage 1.yes 2.no: "))
    if(t==1):
        pr=int(input("enter tip percentage then: "))
        tr=int(amt)*(pr/100)
        print(f"amount each person has to pay is {tr}")
    else:
        p=(amt)/n
        print(f"amount each person has to pay is {p}")
main()
