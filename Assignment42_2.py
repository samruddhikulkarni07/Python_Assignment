import numpy as np
import pandas as pd

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variables X :  -",X)
    print("Values of dependent variables : Y -",Y)
    
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_mean is :",mean_X)     
    print("Y_mean is :",mean_Y)  

    n = len(X)      

    # y = mx + c

    # m = (summ (x-x_bar)*(y-y_bar))/(summ (x-x_bar)**2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_X) * (Y[i]-mean_Y))
        denominator = denominator + ((X[i]-mean_X)**2)

    m = numerator/denominator
    print("Slope of line is :",m)       

    C = mean_Y - (m*mean_X)
    print("Y intercept of line is :",C)     

    Yp = list()
    
    for i in range(n):
        i = m*X[i]+C
        Yp.append(i)

    print(Yp)

    Yp = [float(X) for X in Yp]
    print("predicted values of y:",Yp)

    sum = 0
    for i in range(n):
        sum = sum+((Y[i]-Yp[i])**2)

    MSE = sum/n
    print("Mean squared error is:",MSE)
    

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator+((Yp[i]-mean_Y)**2)
        denominator = denominator+((Y[i]-mean_Y)**2)

    R2 = numerator/denominator
    print("R square value:",R2)


    

    
def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()