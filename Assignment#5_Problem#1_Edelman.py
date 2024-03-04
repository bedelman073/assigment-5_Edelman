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
