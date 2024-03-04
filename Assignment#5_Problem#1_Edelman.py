# creating a class for basic math operations
class BasicMathOperations:
    # creating a function that takes in a first name and last name as inputs and returns a greeting
    def GreetUser(self,f_n,l_n):
        print(f"Hello {f_n} {l_n}")
    # creating a function that takes in two numbers and returns the sum
    def AddNumbers(self,num1,num2):
        return num1+num2
    # creating a function that adds, subtracts, multiplies, or divides a number based on a string input
    def PerformOp(self,num1,num2,operator):
        if operator.upper()=="A":
            return num1+num2
        if operator.upper()=="S":
            return num1-num2
        if operator.upper()=="M":
            return num1*num2
        if operator.upper()=="D":
            if num2==0:
                return "infinity"
            else:
                return num1/num2
    # creating a function that returns the square of a number
    def calculateSqare(self,num):
        return num**2
    # creating a function that retuns the factorial of a number
    def factorial(self,num):
        if num==0:
            return 1
        fact=1
        for i in range(1,num+1):
            fact*=i
        return fact
    # creating a function that returns a list that counts between the inputted numbers
    def count(self,num1,num2):
        count_list=[i for i in range(num1,num2+1)]
        return count_list
    # creating a function that takes in sides of a right triangle and returns the hypotenuse
    def calculateHypotenuse(self,num1,num2):
        hyp=(self.calculateSquare(num1)+self.calculateSquare(num2))**.5
        return hyp
    # creating a function that takes in a width and a height and returns the area of a rectangle
    def AoR(self,width,height):
        return width*height
    # creating a function that raises an inputted base to an inputted power and returns the value
    def PoN(self,base,exp):
        return base**exp
    # creating a function that returns the type of the inputted number
    def numType(self,num):
        num1=eval(num)
        return type(num1)
def main():
    # initalizing an instance of BasicMathOperations
    BMO=BasicMathOperations()
    # creating a while loop that runs while cont=True
    cont=True
    while cont == True:
        BMO.GreetUser("Ben","Edelman")
        print("""Welcome to the basic math operation calculator!
Please enter the number of the function you would like to access.
1.) Add Numbers
2.) Perform Operation (A/S/M/D)
3.) Square Number
4.) Factorial
5.) Counting
6.) Compute Hypotenuse
7.) Area of a Rectangle
8.) Power of a Number
9.) Type of Argument""")
        ans=int(input())
        # getting user input depending on what function the user wants to access, and calling the appropriate method
        if ans == 1:
            num1=float(input("Enter your first number: "))
            num2=float(input("Enter your second number: "))
            print(BMO.AddNumbers(num1,num2))
        if ans == 2:
            num1=float(input("Enter your first number: "))
            num2=float(input("Enter your second number: "))
            operator=input("Enter the operator you would like to use (A/S/M/D): ")
            print(BMO.PerformOp(num1,num2,operator))
        if ans == 3:
            num1=float(input("Enter a number to calcualte its square: "))
            print(BMO.calculateSquare(num1))
        if ans == 4:
            num1=int(input("Enter an integer to find the factorial of it: "))
            print(BMO.factorial(num1))
        if ans == 5:
            num1=int(input("Enter an integer to start with: "))
            num2=int(input("Enter an integer to end with: "))
            print(BMO.count(num1,num2))
        if ans == 6:
            num1=float(input("Enter your first number: "))
            num2=float(input("Enter your second number: "))
            print(BMO.calcualteHypotenuse(num1,num2))
        if ans == 7:
            num1=float(input("Enter the width: "))
            num2=float(input("Enter the height: "))
            print(BMO.AoR(num1,num2))
        if ans == 8:
            num1=float(input("Enter the base: "))
            num2=float(input("Enter the exponent: "))
            print(BMO.PoN(num1,num2))
        if ans == 9:
            num=(input("Enter your number: "))
            print(BMO.numType(num))
        # asking if the user wants to use another function, if they do, the while loop continues. Otherwise, the program ends.
        ans1=input("Do you want to use another function? Enter Y for Yes and N for No: ")
        if ans1.upper()=="Y":
            cont=True
        if ans1.upper()=="N":
            cont=False
        else:
            print("Please enter a valid answer")
main()
