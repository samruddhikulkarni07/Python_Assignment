import numpy as np
import pandas as pd

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variables : X -",X)
    print("Values of dependent variables : Y -",Y)
    
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_mean is :",mean_X)     #3.0
    print("Y_mean is :",mean_Y)     #3.6

    n = len(X)      # 5

    # Y = mx + c

    # m = (summ (X-X_bar)*(Y-Y_bar))/(summ (X-X_bar)**2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_X) * (Y[i]-mean_Y))
        denominator = denominator + ((X[i]-mean_X)**2)

    m = numerator/denominator
    print("Slope of line is :",m)     

    C = mean_Y - (m*mean_X)
    print("Y intercept of line is :",C)    

    

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()