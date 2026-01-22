def ChkPrime(No):
    if (No<2):
        return False
    
    for i in range(2,No):
        if(No%i==0):
            return False

    return True