def finding_gcd(a,b):
    while(b !=0):
        result = b
        a, b= b, a % b
        print("a:",a)
        print("b:", b)
    return result

if __name__ == '__main__':
     a = finding_gcd(12,21)
     print("final result", a)

    