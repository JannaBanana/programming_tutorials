n = int(input("N= "))

array = [[0 for i in range (n+1)] for j in range (n+1)]
x = 0
a = 3
count = 1
count_end = n * n
y = a-1
x_limit = a-1
y_limit = 0
i=0
j=0

for _ in range (2):
    array [i][j]= count
    count += 1
    j=j+1
i = 1
j=1
for _ in range (2):
    array [i][j]=count
    count += 1
    j=j-1

while count < count_end:
    



    for _ in range (a-1):
        array [y][x] = count
        count += 1
        x += 1 # x = x + 1
        if x > x_limit:
            x = x_limit
            break
    for _ in range (a):
        array [y][x] = count
        count += 1
        y=y-1
        if y < y_limit:
            y = y_limit
            x = x+1
            y_limit=x_limit+1
            break
    for _ in range (a+1):
        array [y][x] = count
        count += 1
        y += 1
        if y>y_limit:
            y=y_limit
            x=x-1
            x_limit=0
            break
    for _ in range (a):
        array [y][x] = count
        count += 1
        x -= 1
        if x<x_limit:
            x=x_limit
            y=y+1
            a=a+2
            y_limit=0
            x_limit=a-1
            break

for i in range(n):
    for j in range(n):
        print(array[i][j], ' ', end="")
    print()
