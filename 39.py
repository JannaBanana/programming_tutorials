str = input("N, M = ")
str_split = str.split(', ')
n = str_split[0]
m = int(str_split[1])
mid = (m+1)//2

for c in range(mid):
    a = ord(n) - 1
    for b in range (m):
        if b < (m+1)//2:
            a += 1
        else:
            a -= 1

        if a - ord(n) < mid - 1 - c:
            print("_  ", end="")
        else:
            if a>90:
                print(chr(a-26), " ", end="")
            else:
                print(chr(a), " ", end="")
    print()
