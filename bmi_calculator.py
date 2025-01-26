def main():
    w=int(input("enter your weight: "))
    h=int(input("enter your height: "))
    bmi=w/(h*h)
    print(f"BMI value is {bmi}")
    if bmi<18.5:
        print("underweight")
    elif bmi>=18.5 and bmi<=24.9:
        print("Normal")
    elif bmi>=25 and bmi<=29.9:
        print("overweight")
    elif bmi>=30 and bmi<=34.9:
        print("obese")
    else:
        print("extreme obese")
main()