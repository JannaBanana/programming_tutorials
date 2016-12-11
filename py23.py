n = int(input("insert N: "))

array = [[" " for _ in range (2*n-1)] for _ in range (n)]


for a in range (1,n+1):
    x = n-a
    y = a-1
    b = 1
    for _ in range (1,a+1):
        array [y][x] = b
        b += 1
        x += 2

for i in range(n):
    for j in range(n*2-1):
        print (array[i][j], end="")
    print("")
