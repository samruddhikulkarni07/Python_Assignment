No = 0
print("Enter a number:")
No = int(input())

Reverse = 0

while(No>0):
    digit = No % 10
    Reverse = Reverse * 10 + digit
    No = No // 10

print("Reverse of given number is:",Reverse)  