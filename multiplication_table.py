def display_table(n,r):
    for i in range(1,r+1):
        print(f"{n} * {i} = {n*i}")    
def main():
    n=int(input("enter number: "))
    r=int(input("enter range: "))
    display_table(n,r)
main()