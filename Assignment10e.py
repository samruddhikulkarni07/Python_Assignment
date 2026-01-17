N = 0
print("Enter a number:")
N = int(input())

print("All odd numbers till",N,"are:")
for i in range(1,N+1):
    if (i%2==1):
        #print(i)    gives each number in separate line
        print(i,end=" ")        #gives all numbers in a single line

