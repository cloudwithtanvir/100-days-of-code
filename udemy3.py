n = int(input())
m = int(input())
array1 = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        array1[i][j] =i,j
print(array1)