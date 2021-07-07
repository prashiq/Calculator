

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Operators:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divide")



while True:

    num1 = float(input("Enter a number: "))

    choice = input("Enter operator number(1/2/3/4): ")

    num2 = float(input("Enter second number: "))

    if choice in ('1','2','3','4'):

        if choice == "1":
             print(num1,"+",num2,"=",add(num1,num2))

        elif choice == "2":
             print(num1,"-",num2,"=",subtract(num1,num2))

        elif choice == "3":
             print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice == "4":
             print(num1,"/",num2,"=",divide(num1,num2))
        else:
            print("Invalid Intput")
    else:
        print("Invalid Input")
