num = int(input("Enter the Number:"))

if(num<=1):
    print("Not a prime number")
else:
    for i in range(2,num):
        if (num % 2 == 0):
            print("Not a prime number")
            break
    else:
        print("Prime Number")