odd_list=[]
even_list=[]
def main():
    n=int(input("enter size: "))
    list=[]
    print("enter number: ")
    for i in range(n):
        x=int((input()))
        list.append(x)
        if x%2==0:
            even_list.append(x)
        else:
            odd_list.append(x)
        # print(list[i])
    print("even list numbers are ")
    for a in even_list:
        print(a)
    print("odd list numbers are ")
    for b in odd_list:
        print(b)
main()