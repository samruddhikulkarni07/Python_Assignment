No = 0
print("Enter a number:")
No = int(input())

sum = 0

while(No>0):
    carry = No % 10         # gives carry
    sum = sum + carry
    No = No // 10           # gives quotient as int 

print("Sum of digits in given number:",sum)