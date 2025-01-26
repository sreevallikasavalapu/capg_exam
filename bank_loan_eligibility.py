def main():
    print("hello, want to check your loan eligibility")
    sal=int(input("enter your salary"))
    age=int(input("enter your age"))
    credit_score=int(input("enter your credit score"))
    if sal>=50000:
        if age>18:
            if credit_score>800:
                print("Loan is approved")
            else:
                print("loan rejected due to your credit score")
        else:
            print("loan rejected")
            print("reason: age doesn't match the criteria")
    else:
        print("loan rejected ")
        print("reason: your salary is low")
main()