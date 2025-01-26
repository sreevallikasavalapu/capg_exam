def check_prime(n):
    if n < 2:  
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

def main():
    while True:
        start = int(input("Enter the start of the range (a): "))
        end = int(input("Enter the end of the range (b): "))
        
        # Validating input
        if start < 1 or end < 1 or end > 10000 or start > end:
            print("Invalid input. Please enter valid numbers within the range (1 <= a <= b <= 10000).")
            continue
        
        print(f"Prime numbers between {start} and {end} are:")
        for i in range(start, end + 1):
            if check_prime(i):
                print(i, end=" ")
        print()  
        break 

main()
