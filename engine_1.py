lis = ['32 + 50']
lis2 = ['70 - 22']


def formatter(list):
    sprt = ' '.join(list)  # split the list into string
    a = sprt.rsplit()  # split the string into list

    # print(type(sprt))  # debug the type of sprt

    # print(sprt)  # debug the result of sprt

    # print(a)  # debug the result of a

    # print(type(a))  # debug the type of a
    if a[1] == '+':
        total = int(a[0]) + int(a[2])
        print(total)
    elif a[1] == '-':
        total = int(a[0]) - int(a[2])
        print(total)



formatter(lis)
formatter(lis2)

