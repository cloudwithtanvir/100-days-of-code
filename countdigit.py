s = input()
d=0
n=0
for i in s:
    if i.isdigit():
        d=d+1

    elif i.isalpha():
        n=n+1  
    else:
        pass      
print(d)
print(n)        