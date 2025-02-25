def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
def fibo(num):
    a,b=0,1
    print("The fibonacci series is:")
    for _ in range(1,num+1):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
    print("")
def prime(number):
    c=0
    for i in range(2,int(number/2)):
        if(number%i==0):
            c+=1
            break
    if(c==0):
        return 1
    else:
        return 0
    
while(1):
    print("Enter 1 for factorial, 2 for fibonacci series, 3 for prime number and other for exit:")
    n=int(input(""))
    if(n==1):
        b=int(input("Enter a number:"))
        f=fact(b)
        print(f"Factorial of {b} is:{f}")
    elif(n==2):
        b=int(input("Enter the number of terms:"))
        fibo(b)
    elif(n==3):
        b=int(input("Enter a number:"))
        p=prime(b)
        if(p==1):
            print(f"{b} is a prime number")
        else:
            print(f"{b} is not a prime number")
    else:
        break
    

        