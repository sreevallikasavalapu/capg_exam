numbers=[]
temp1,temp2=0,0
n=int(input("enter size: "))
print("enter elements :")
for i in range(n):
    m=int(input())
    numbers.append(m)
    # temp1=m
    if m>temp1:
        temp2=temp1
        temp1=m
    else:
        if m>temp2 and temp2!=temp1:
            temp2=m
# print(temp1)
print(f"second largest number is {temp2}")