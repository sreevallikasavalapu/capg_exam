
def check_balance(bal):
    print(f"balance amount is {bal}")
def deposit_money(bal):
    amt=int(input("enter amount"))
    bal+=amt
    print("deposited")
    return bal
def withdraw_money(bal):
    if bal==0:
        print("insufficient balance")
    else:
        print("initiating....")
        print("money successfully withdrawn")
def main():
    bal=0
    
    while True:
        # print("enter choice 1.check balance 2.deposit money 3.withdraw money 4.exit : ")
        n=int(input("enter choice 1.check balance 2.deposit money 3.withdraw money 4.exit : "))
        if n==4:
            break
        elif n==1:
            check_balance(bal)
            # continue
        elif n==2:
            
            bal+=deposit_money(bal)
            
        elif n==3:
            withdraw_money(bal)
            # continue
        else:
            print("enter correct choice: ")
            continue
main()