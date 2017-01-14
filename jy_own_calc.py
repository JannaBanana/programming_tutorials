whole_calculus = input("input: ")
# whole_calculus = 10*5+10-3*10

def list_x (x):
    y = []
    len_x = len(x)
    operator = ['+', '-', '*', '/']
    for i in range (len_x):
        if list(x)[i] in operator:
            y = y + [' ', list(x)[i], ' ']
        else:
            y = y + [list(x)[i]]
    y = ''.join(y)
    # ['1', '0', ' ', '*', ' ', '5', ' ', '+', ' ', ...] = 10 * 5 + 10 - 3 * 10
    y = y.split(" ")
    # 10 * 5 + 10 - 3 * 10 = ['10', '*', '5', '+', '10', '-', '3', '*', '10']
    return y
# list_x (x) = 10*5+10-3*10 >> ['10', '*', '5', '+', '10', '-', '3', '*', '10']

def multiple_devide_x (x):
    len_x = len(x)
    print("list(x)[0:len_x]= ", x, "and", list(x)[0:len_x])
    y = int(list(x)[0])
    for i in range (len_x):
        if list(x)[i] == '*':
            y = y * int(list(x)[i+1])
        elif list(x)[i] == '/':
            y = y / int(list(x)[i+1])
    y = str(y)
    print("y=", y)
    return y
# multiple_devide_x (x) = ['3', '*', '10', '/', '5'] = ['6']

def minus_plus_x (x):
    y = int(list(x)[0])
    len_x = len(x)
    for i in range (len_x):
        if list(x)[i] == '+':
            y = y + int(list(x)[i+1])
        elif list (x)[i] == '-':
            y = y - int(list(x)[i+1])
    return y


split_calculus = list_x (whole_calculus)
# split_calculus = ['10', '*', '5', '+', '10', '-', '3', '*', '10']
print ("split_calculus= ", split_calculus)
len_split_calculus = len(split_calculus)
multiple_devide = []
multiple_devide_value = []
i = 0

while i< len_split_calculus :
    if list(split_calculus)[i] in ('*', '/'):
        for j in range (i, len_split_calculus):
            if list(split_calculus)[j] in ('+', '-'):
                multiple_devide = list(split_calculus)[i-1:j] #multiple_devide = ['10', '*', '5']
                multiple_devide_value[len(multiple_devide_value)-1] = multiple_devide_x (multiple_devide)
                i = j
                break
            elif j == (len_split_calculus-1):
                multiple_devide = list(split_calculus)[i-1:j+1] #multiple_devide = ['3', '*', '10']
                multiple_devide_value[len(multiple_devide_value) - 1] = multiple_devide_x(multiple_devide)
                i = j+1
                break
    else:
        multiple_devide_value = multiple_devide_value + [list(split_calculus)[i]]
        i += 1
# multiple_devide_value = ['50', '+', '10', '-', '30']
print("multiple_devide_value= ", multiple_devide_value)
total_value_of_whole_calculus = minus_plus_x(multiple_devide_value)
print ("total_value_of_whole_calculus= ", total_value_of_whole_calculus)





