class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first value:"))
        self.value2 = int(input("Enter second value:"))

    def Addition(self):
        Add = self.value1 + self.value2
        print("Addition is:",Add)

    def Substraction(self):
        Sub = self.value1 - self.value2
        print("Substraction is:",Sub)

    def Multiplication(self):
        Mul = self.value1 * self.value2
        print("Multiplication is:",Mul)

    def Division(self):
        try:
            Div = self.value1 / self.value2
            print("Division is:",Div)

        except ZeroDivisionError as zobj:
            print("Division by zero is not possible:",zobj)


obj1 = Arithmetic()
obj2 = Arithmetic()
obj3 = Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()
print("\n")

obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()
print("\n")

obj3.Accept()
obj3.Addition()
obj3.Substraction()
obj3.Multiplication()
obj3.Division()
print("\n")
