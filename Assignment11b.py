No = 0
print("Enter a number:")
No = int(input())

count = 0

while(No>0):
    count = count + 1
    No = No // 10           # gives quotient as int 

print("Count of digit in given number:",count)