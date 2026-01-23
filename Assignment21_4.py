import threading
sum = 0
mul = 1

def DisplaySum(data):
    global sum

    for i in data:
        sum = sum + i

    
def DisplayProduct(data):
    global mul

    for i in data:
        mul = mul * i

    
def main():
    global sum
    global mul

    No = int(input("Enter number of elements:"))
    value = 0
    Data = list()

    print("Enter elements:")

    for i in range(No):
        value = int(input())
        Data.append(value)
    print("Original list:",Data)

    Sum = threading.Thread(target=DisplaySum,args=(Data,))
    Product = threading.Thread(target=DisplayProduct,args=(Data,))

    Sum.start()
    Product.start()

    Sum.join()
    Product.join()

    print("Sum is:",sum)
    print("Product is:",mul)


if __name__ == "__main__":
    main()