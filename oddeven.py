num =(1,2,3,4,5,6,7,8,9)
d=e=0
for i in num:
    if(i%2)==0:
        e=e+1;
    elif(i%2)!=0:
        d=d+1;    
print("odd" ,d)
print("even", e)        