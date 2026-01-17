No = 0
print("Enter a number:")
No = int(input())

original = No
Reverse = 0

while(No>0):
    digit = No % 10
    Reverse = Reverse * 10 + digit
    No = No // 10

if(original == Reverse):
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")
