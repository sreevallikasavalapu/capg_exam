def check_palindrome(n):
    rev=n[::-1]
    if n==rev:
        return True
    else:
        return False
def main():
    while True:
        n=input("enter input")
        if check_palindrome(n):
            print(f"{n} is palindrome")
        else:
            print(f"{n} is not a palindrome")
main()
            
        