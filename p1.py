# for n in range (1, 11):
#     print (n)


# 1 1
# 1 2
# 1 3
# ...
# 1 10
#...
# 10 10
#
# test = list(range(1, 11))
# for n in test:
#     print(n)

# for n in range (1,11):
#     for m in range (1,11):
#         print (n, m)

#n = int(input("숫자를 입력해주세요: "))
#print(n, type(n))


n = int(input("insert: "))

for i in range (0,2*n-1):
    if i < n:
        for j in range (0, n):
            if i >=j:
                print (1, " ", end="")
    else:
        for j in range (n, 2*n):
            if i < j:
                print (1, " ", end="")
    print("\n")
