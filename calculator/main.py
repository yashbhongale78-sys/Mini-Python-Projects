def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a = True
while a :
    try: 
        a = int(input("Enter num 1: "))
        b = int(input("Enter mum 2: "))
        print("what kind of operation do you want to perform ?")
        print("1 for Multiplication")
        print("2 for divis")
        print("3 for add")
        op = int(input("Enter operation"))


        match op:
            case 1:
                print("Multiplication is :",mul(a,b))
            case 2:
                print("Divsion is :",div(a,b))
            case 3:
                print("addition is ",add(a,b))
            case default:
                print("Error")


    except Exception as e: 
        print("enter valid values of a and b ")


    print("repeat operation y/n")
    x = input("")
    if x == 'y':
        a= True
    else :
        a = False
        