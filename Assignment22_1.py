class Demo:
    value = 10
    
    def __init__(self,A,B):
        self.value1 = A
        self.value2 = B

    def Fun(self):
        print("Value of instance variables:",self.value1,self.value2)

    def Gun(self):
        print("Value of instance variables:",self.value1,self.value2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()
