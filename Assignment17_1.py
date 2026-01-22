import Arithmetic

No1 = int(input("Enter first number:"))
No2 = int(input("Enter second number:"))
Result = 0

Result = Arithmetic.Add(No1,No2)
print("Addition is:",Result)

Result = Arithmetic.Sub(No1,No2)
print("Substraction is:",Result)

Result = Arithmetic.Mul(No1,No2)
print("Multiplication is:",Result)

Result = Arithmetic.Div(No1,No2)
print("Division is:",Result)