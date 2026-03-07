import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    #Feature:Experience
    X = [1,2,3,4,5]

    #label : salary
    Y = [20000,25000,30000,35000,40000]

    print("Values of independent variables X :  -",X)
    print("Values of dependent variables : Y -",Y)
    
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_mean is :",mean_X)     #3.0
    print("Y_mean is :",mean_Y)     #3.6

    n = len(X)      # 5

    # y = mx + c

    # m = (summ (x-x_bar)*(y-y_bar))/(summ (x-x_bar)**2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_X) * (Y[i]-mean_Y))
        denominator = denominator + ((X[i]-mean_X)**2)

    m = numerator/denominator
    print("Slope of line is :",m)       #0.4

    C = mean_Y - (m*mean_X)
    print("Y intercept of line is :",C)     #2.4

    X_new = 6
    Yp= m*X_new+C
    print("predicted value of X_new :",Yp)

    

    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color = 'y',label = "Regression Line" )
    
    plt.legend()
    plt.xlabel("X:Indepenent Vriables")
    plt.ylabel("Y:Dependent Variables")
    plt.show()
    
def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()