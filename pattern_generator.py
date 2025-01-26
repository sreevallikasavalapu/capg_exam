def print_normal(n):
    for i in range(1,n+1):
        print("*"*i)
def print_reverse(n):
    for i in range(n,0,-1):
        print("*"*i)
def main():
    n=int(input("enter number: "))
    ch=int(input("enter choice 1.pyramid print 2.reverse print :"))
    if ch==1:
        print_normal(n)
    else:
        print_reverse(n)
main()
