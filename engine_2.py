def formatter(list):
    # second split the data
    sprt = ' '.join(list)  # split the list into string
    split_str = sprt.rsplit()  # split the string into list

    # third make new variable for container
    result = None

    # forth separate the which is addition or subtraction
    if split_str[1] == '+':
        total = int(split_str[0]) + int(split_str[2])
        result = total
    elif split_str[1] == '-':
        total = int(split_str[0]) - int(split_str[2])
        result = total

    # fifth store the result inside the new variable
    a = split_str[0]
    b = split_str[2]
    nota = split_str[1]

    return result, a, b, nota


def arithmetic_arranger(problems):
    # first format the list data input
    new_list = [problems[i:i + 1] for i in range(0, len(problems), 1)]

    # sixth make new empty variable
    data = []

    # appending the new_list into empty data list variable
    for n in range(len(new_list)):
        data.append(formatter(new_list[n]))
    print(data)

    print(data[0][1])
    print('\n')
    for n in data:
        for i in n:
            print('n : ', n)
            print('i : ', i)

    # formatting the output
    # for n in range(len(data)):
    #     rslt, num1, num2, nt = data[n]
    #     frmt = f'''
    #             {num1}
    #           {nt} {num2}
    #             -----
    #             {rslt}
    #             '''
        # print(frmt)
        # return frmt





arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])