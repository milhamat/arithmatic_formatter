def arithmetic_arranger(problems):
    # first format the list data input
    new_list = [problems[i:i + 1] for i in range(0, len(problems), 1)]

    # second split the data
    sprt = ' '.join(new_list)  # split the list into string
    split_str = sprt.rsplit()  # split the string into list

    # third make new variable for container
    a = None
    b = None
    result = None
    nota = ''

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






arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])