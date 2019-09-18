n =int(input(""))
for i in range(0,n):
    x=int(input())
    for j in range(2,x):
        if (x%j)==0:
            print(x,"is not prime")
            break
    else:
        print(x,"is prime")        
