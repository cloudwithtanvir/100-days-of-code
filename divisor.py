n =int(input())
for i in range(0,n):
    x=int(input())
    for j in range(1,x+1):
        if(x%j)==0:
            print(j)
