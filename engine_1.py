lis = ['32 + 50']
lis2 = ['70 - 22']


def formatter(list):
    sprt = ' '.join(list)  # split the list into string
    split_str = sprt.rsplit()  # split the string into list

    if split_str[1] == '+':
        total = int(split_str[0]) + int(split_str[2])
        print(total)
    elif split_str[1] == '-':
        total = int(split_str[0]) - int(split_str[2])
        print(total)



formatter(lis)
formatter(lis2)

