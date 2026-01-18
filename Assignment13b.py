def Area(x):
    PI = 3.14
    return 2*PI*x

def main():
    radius = int(input("Enter radius of circle:"))

    area = 0

    area = Area(radius)
    print("Area of circle:",area)

if __name__ == "__main__":
    main()