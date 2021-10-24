list_1 = [['32 + 50'],
          ['20 - 50'],
          ['32 + 10']]
# actually the code up there is matrix


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

    return result, a, b, nota


data = []

for n in range(len(list_1)):
    # print(list_1[n])
    data.append(formatter(list_1[n]))

print(data)

# try to query the tuple nested in list
print(data[0])

# try query more
for n in range(len(data)):
    rslt, num1, num2, nt = data[n]
    print(rslt)


# print(len(data))