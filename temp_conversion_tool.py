def cel_to_fah():
    c=input("enter celsius:")
    f=int(c)*(9/5)+32
    print(f"value is {f}")
def fah_to_cel():
    f=input("enter fahrenheit:")
    c= 5*(f-32)/9
    print(f"value is {c}")
def kel_to_cel():
    k=input("enter kelvin value:")
    c=k-273.15
    print(f"value is {c}")
def cel_to_kel():
    c=input("enter celsius:")
    k=c+273.15
    print(f"value is {k}")
def fah_to_kel():
    f=input("enter fahrenheit:")
    k=(f-32)*(5/9)+273.15
    print(f"value is {k}")
def kel_to_fah():
    k=input("enter kelvin value:")
    f=(k-273.15)*(9/5)+32
    print(f"value is {f}")
def main():
    n=int(input("enter choice 1.celsius to fahrenheit 2.fahrenheit to celsius 3.kelvin to celsius 4.celsius to kelvin 5.fahrenheit to kelvin 6.kelvin to fahrenheit "))
    if n==1:
        cel_to_fah()
    elif n==2:
        fah_to_cel()
    elif n==3:
        kel_to_cel()
    elif n==4:
        cel_to_kel()
    elif n==5:
        fah_to_kel()
    elif n==6:
        kel_to_fah
    else:
        print("wrong choice")
main()