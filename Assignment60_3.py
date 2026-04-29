import numpy as np
import math

def Binary_Cross_Entropy(Actual,Predicted):
    n = len(Actual)
    total_loss = 0

    for i in range(n):
        y = Actual[i]
        pr = Predicted[i]

        p = max(min(pr,0.999),0.001)

        loss = -(y*math.log(p)+(1-y)*math.log(1-p))
        total_loss+=loss

    return total_loss/n
        

def MSE(Actual,Predicted):
    n = len(Actual)
    total_error = 0

    for i in range(n):
        error = Actual[i] - Predicted[i]
        total_error += error ** 2

    return total_error/n


def main():
    Actual = [10,20,30]
    Predicted = [11,19,32]

    mse = MSE(Actual,Predicted)
    print("Mean Squared error:",mse)

    bce = Binary_Cross_Entropy(Actual,Predicted)
    print("Binary_Cross_Entropy :",bce)

if __name__ == "__main__":
    main()