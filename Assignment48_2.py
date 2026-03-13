import numpy as np

def main():

    X = [6,7,8,9,10,11,12]
    
    #---------------------------------
    # Step 1 : mean
    #---------------------------------

    mean = np.mean(X)
    print("Mean is:",mean)

    #---------------------------------
    # Step 2 : variance
    #---------------------------------

    # variance = summ (X-mean)**2/n

    numerator = 0

    for i in X:
        numerator = numerator + ((i-mean)**2)

    variance = numerator/7   #  n = 7

    print("Variance is:",variance)

    #---------------------------------
    # Step 3 : Standard deviation
    #---------------------------------

    # Standard deviation = under root of variance
  
    standard_deviation = np.sqrt(variance)
    print("Standard deviation is :",standard_deviation)



if __name__ == "__main__":
    main()