def leap_check(n):
    if n%4==0 or n%400==0:
        return True
    else:
        return False
def main():
    while True:
        n=int(input("enter year: "))
        if (leap_check(n)):
            print(f"{n} is a leap year")
        else:
            print(f"{n} is not a leap year")
main()
    