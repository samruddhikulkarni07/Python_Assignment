from sklearn.preprocessing import StandardScaler

def main():

    X = [[25,20000],
        [30,40000],
        [35,80000]
    ]

    scaler = StandardScaler()
    Scaled_X = scaler.fit_transform(X)

    print(Scaled_X)
    
   
    
if __name__ == "__main__":
    main()