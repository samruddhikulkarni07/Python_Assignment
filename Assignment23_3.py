class Numbers:
    Value = 0

    def __init__(self):
        Numbers.Value = int(input("Enter a number:"))

    def ChkPrime(self):
        if(Numbers.Value<=1):
            return False
        
        for i in range(2,Numbers.Value):
            if(Numbers.Value % i == 0):
                return False
        return True        
            

    def Factors(self):
        factors = []
        for i in range(1,Numbers.Value):
            if(Numbers.Value % i == 0):
                factors.append(i)
        return factors

    def SumFactors(self):
        total = 0
        for i in range(1,Numbers.Value):
            if(Numbers.Value % i == 0):
                total = total + i
        return total

    def ChkPerfect(self):
        return self.SumFactors()==Numbers.Value
           

obj1 = Numbers()

print("Prime Number:",obj1.ChkPrime())
print("Factors are:",obj1.Factors())
print("Sum of Factors is:",obj1.SumFactors())
print("Perfect Number:",obj1.ChkPerfect())
print("\n")

obj2 = Numbers()

print("Prime Number:",obj2.ChkPrime())
print("Factors are:",obj2.Factors())
print("Sum of Factors is:",obj2.SumFactors())
print("Perfect Number:",obj2.ChkPerfect())
print("\n")

obj3 = Numbers()

print("Prime Number:",obj3.ChkPrime())
print("Factors are:",obj3.Factors())
print("Sum of Factors is:",obj3.SumFactors())
print("Perfect Number:",obj3.ChkPerfect())
print("\n")
    