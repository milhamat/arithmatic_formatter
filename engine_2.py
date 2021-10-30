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

    return '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'




arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])