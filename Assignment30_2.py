def main():
    wordscount = 0
    fname = input("Enter a file name:")

    fobj = open(fname,"r")

    for line in fobj:               #reads file line by line
        words = line.split()
        wordscount = wordscount+len(words)

    fobj.close()

    print(f"Numbers of words in {fname} are:",wordscount)

    
if __name__ == "__main__":
    main()