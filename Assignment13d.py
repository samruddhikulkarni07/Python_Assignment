def main():
    no = int(input("Enter a number:"))

    binary = " "

    while(no>0):
        binary = str(no % 2) + binary
        no = no // 2

    print("Binary equivalent of number is:",binary)

if __name__ == "__main__":
    main()
