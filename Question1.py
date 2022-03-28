class Calculator:
    
    def __init__(self, first, second):
        self.first = first;
        self.second = second;
    
    #Add 
    def adder(self):
        return self.first + self.second
    
    #Subtract 
    def subtractor(self):
        return self.first - self.second

    #Mulitply 
    def multiplier(self):
        return self.first * self.second

    #Divide 
    def divider(self):
        return self.first / self.second
    
    #Reset to 0
    def clear(self):
        self.first = 0
        self.second = 0

#Input from user
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

#create a variable to pass in the parameters needed in the class calculator
cal = Calculator(firstNumber, secondNumber)

#Print the different types of calculation
print("Addition: ", cal.adder())
print("Subtraction: ", cal.subtractor())
print("Multiplication: ", cal.multiplier())
print("Division: ", cal.divider())
cal.clear()
print(cal.first, cal.sec)
