print("     ..........Welcome TO Calculator..........     ")
print("")
print("---------------------------------------------------")

class Calculator:
    def add(self, result=0):
        while True:
            no = input("Enter Numbers for Addition... ")
            if (no == "" or no == " "):
                break
            else:
                result += int(no)
                print("Total is : ",result)
        print("Addition is ", result)
        print()
        option()

    def sub(self):
        result = input("Enter Number for Subtraction ")
        if(result==""):
            print("Calculator Ended... Thank You!!!")
        else:   
            while True:
                no = input("Enter numbers for subtraction ")
                if (no == "" or no == " "):
                    break
                else:
                    result =int(result) - int(no)
                    print("Total is : ",result)
            print("Subtraction is ", result)
            print()
            option()

    def mul(self):
        result = input("Enter Number for Multiplication ")
        if(result==""):
            print("Calculator Ended... Thank You!!!")
        else:
            while True:
                no = input("Enter Numbers for Multiplication ")
                if (no == "" or no == " "):
                    break
                else:
                    result =int(result) * int(no)
                    print("Total is : ",result)
            print("Multiplication is ", result)
            print()
            option()

    def div(self):
        result = input("Enter Number for Division ")
        if(result==""):
            print("Calculator Ended... Thank You!!!")
        else:
            while True:
                no = input("Enter Numbers for Division ")
                if (no == "" or no == " "):
                    break
                else:
                    result =int(result) / int(no)
                    print("Total is : ",result)
            print("Division is ", result)
            print()
            option()

    def mod(self):
        result = input("Enter Number to check modulus ")
        if(result==""):
            print("Calculator Ended... Thank You!!!")
        else:
            while True:
                no = input("Enter Number to check Modulus")
                if (no == "" or no == " "):
                    break
                else:
                    result =int(result) % int(no)
                    print("Total is : ",result)                
            print("the Modulus is  ",result)
            print()
            option()

    def expo(self):
        result = input("Enter Number")
        if(result==""):
            print("Calculator Ended... Thank You!!!")
        else:
            no = input("Enter Numbers ")
            result = int(result) ** int(no)
            print("Exponential is ", result)
            print()
            option()

    def flo(self):
        result = input("Enter Number ")
        if(result==""):
            print("Calculator Ended... Thank You!!!")
        else:
            while True:
                no = input("Enter Numbers ")
                if no == "" or no == " ":
                    break
                else:
                    result = int(result) // int(no)
                    print("Total is : ",result)
            print("Floor Division is ", result)
            print()
            option()


def option():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponential")
    print("7. Floor Division")
    print("Press Enter To Exit ")
    op = input("Enter Your Choice.. ")
    cal = Calculator()
    if (op=="" or op==" "):
        print("Calculator Ended... Thank You!!!")
    elif(op.lower()=="addition"):
        cal.add()
    elif(op.lower()=="subtraction"):
        cal.sub()
    elif(op.lower()=="multiplication"):
        cal.mul()
    elif(op.lower()=="division"):
        cal.div()
    elif(op.lower()=="modulous"):
        cal.mod()
    elif(op.lower()=="exponential"):
        cal.expo()
    elif(op.lower()=="floor division"):
        cal.flo()
    elif (op == '1'):
        cal.add()
    elif (op == '2'):
        cal.sub()
    elif (op == '3'):
        cal.mul()
    elif (op == '4'):
        cal.div()
    elif (op == '5'):
        cal.mod()
    elif (op == '6'):
        cal.expo()
    elif (op == '7'):
        cal.flo()
    else:
        print("Sorry But We Don't Have That Calculation or you just mistyped something.. Please Try Again")
        option()

option()
