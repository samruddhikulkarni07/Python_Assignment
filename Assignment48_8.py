from sklearn.metrics import confusion_matrix

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    cm = confusion_matrix(actual,predicted)
    print(cm)

    tp,fn,fp,tn = cm.ravel()
    print("TP:",tp)
    print("FN:",fn)
    print("FP:",fp)
    print("TN:",tn)


if __name__ == "__main__":
    main()