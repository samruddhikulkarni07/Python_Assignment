def Area(x,y):
    return x*y

def main():
    length = int(input("Enter length of rectangle:"))
    width = int(input("Enter width of rectangle:"))

    area = 0

    area = Area(length,width)
    print("Area of rectangle:",area)

if __name__ == "__main__":
    main()