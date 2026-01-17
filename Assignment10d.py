N = 0
print("Enter a number:")
N = int(input())

print("All even numbers till",N,"are:")
for i in range(1,N+1):
    if (i%2==0):
        #print(i)    gives each number in separate line
        print(i,end=" ")        #gives all numbers in a single line

