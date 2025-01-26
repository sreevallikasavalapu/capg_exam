n=int(input("enter number"))
if n<1:
    print("negative number")
else:
    val=1
    for i in range(1,n+1):
        val*=i
    print(f"factorial of {n} is {val}")