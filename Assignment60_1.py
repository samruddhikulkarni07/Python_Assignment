import math

def Sigmoid(z):

    return 1/(1 + math.exp(-z))


def Weighted_sum(inputs,weights,bias):

    z = sum(x * w for x, w in zip(inputs,weights))+bias

    z_hat = Sigmoid(z)

    return z, z_hat


def main():

    inputs = [2,3]

    weights = [0.4,0.6]

    bias = 0.5

    z,z_hat = Weighted_sum(inputs,weights,bias)

    print("Weighted sum is :",z)

    print("Output after activation function:",z_hat)


if __name__ == "__main__":
    main()