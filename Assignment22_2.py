class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("Enter radius of circle:"))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        print("Area of circle:",self.Area)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        print("Circumfeence of circle:",self.Circumference)

    def Display(self):
        print("Radius,Area and circumference of circle are:",self.Radius,self.Area,self.Circumference)

obj1 = Circle()
obj2 = Circle()
obj3 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()