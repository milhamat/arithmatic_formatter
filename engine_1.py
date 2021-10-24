lis = ['32 + 50']
lis2 = ['70 - 22']


def formatter(list):
    sprt = ' '.join(list)  # split the list into string
    split_str = sprt.rsplit()  # split the string into list
    a = None
    b = None
    result = None
    nota = ''

    if split_str[1] == '+':
        total = int(split_str[0]) + int(split_str[2])
        result = total
    elif split_str[1] == '-':
        total = int(split_str[0]) - int(split_str[2])
        result = total

    a = split_str[0]
    b = split_str[2]
    nota = split_str[1]

    return result, a, b, nota  # it will return as a tuple



rslt, num1, num2, nt = formatter(lis)
# print(num1, nt, num2, '=', rslt)

frmt = f'''
       {num1}
       {num2}
       ----- {nt}
       {rslt}
       '''
print(frmt)
# formatter(lis2)

