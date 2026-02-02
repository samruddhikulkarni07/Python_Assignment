def main():
    linecount = 0
    fname = input("Enter a file name:")

    fobj = open(fname,"r")

    for line in fobj:
        linecount = linecount+1

    fobj.close()

    print(f"Numbers of line in {fname} are:",linecount)

    
if __name__ == "__main__":
    main()