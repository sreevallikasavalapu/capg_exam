item_list=[]
price_list=[]
# add items view items tot price exit
def add_items(item_name,item_price):
    item_list.append(item_name)
    price_list.append(float(item_price))
def view_items():
    if not item_list:
        print("no items in list")
    else:
        print("items in list are: ")
        for i in item_list:
            print(i)
        print()
def total_price():
    sum=0
    for i in price_list:
        sum+=i
    print(f"total price is {sum}")
def main():
    while True:
        print("select option 1.add items 2.view items 3.total price 4.exit")
        ch=int(input())
        if ch==1:
            a=input("enter item name:")
            b=input("enter item price")
            add_items(a,b)
        elif ch==2:
            view_items()
        elif ch==3:
            total_price()
        elif ch==4:
            break
        else:
            print("wrong choice")
main()