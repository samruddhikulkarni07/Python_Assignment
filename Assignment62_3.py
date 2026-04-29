import numpy as np

matrix = np.array([
    [6,4],
    [8,6]
])
flatten_output = matrix.flatten()

print("Input Matrix:")
print(matrix)

print("\nFlatten Output:")
print(flatten_output)

print("FULLY CONNECTED LAYER")
    
weights = np.array([0.8, 0.5, 0.3, 0.9])
bias = 1.0

print("Flatten Input :", flatten_output)
print("Weights       :", weights)
print("Bias          :", bias)


print("\nInput × Weight:")
multiplication = flatten_output * weights
print("Multipllication is : ",multiplication)
    

total = np.sum(multiplication)

print("\nSum =", total)

final_output = total + bias

print("Final Output = Sum + Bias")
print(f"{total:.2f} + {bias} = {final_output:.2f}")

   