def formatter(list):
    # second split the data
    sprt = ' '.join(list)  # split the list into string
    split_str = sprt.rsplit()  # split the string into list

    # third make new variable for container

    # make error for input a and b
    if len(split_str[0]) >= 5:
        raise TypeError("Numbers cannot be more than four digits.")
    if len(split_str[2]) >= 5:
        raise TypeError("Numbers cannot be more than four digits.")
    try:
        ip1 = int(split_str[0])
        ip2 = int(split_str[2])
    except:
        raise ValueError("Numbers must only contain digits.")

    # forth separate the which is addition or subtraction
    if split_str[1] == '+':
        total = ip1 + ip2
        result = total

    elif split_str[1] == '-':
        total = ip1 - ip2
        result = total

    else:
        raise TypeError("Operator must be '+' or '-'.")

    # fifth store the result inside the new variable
    a = split_str[0]
    b = split_str[2]
    nota = split_str[1]

    return result, a, b, nota


def arithmetic_arranger(problems, answer=False):
    # first format the list data input
    new_list = [problems[i:i + 1] for i in range(0, len(problems), 1)]
    # print(new_list)
    # print(len(new_list))
    if len(new_list) >= 5:
        raise TypeError("Too many problems.")

    # sixth make new empty variable
    data = []

    # appending the new_list into empty data list variable
    for n in range(len(new_list)):
        data.append(formatter(new_list[n]))

    # formatting the output
    for n in range(len(data)):
        rslt, num1, num2, nt = data[n]
        frmt = f'''
                {num1}
              {nt} {num2} 
                -----
                {rslt}
                '''
        frmt2 = f'''
                {num1}
              {nt} {num2} 
                -----
                
                '''
        if answer:
            print(frmt)
        else:
            print(frmt2)
        # return frmt



## normal problem. (ok)
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
## To many problems. (ok)
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49", "123 + 49"],True)
## notation. (ok)
# arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "123 + 49"],True)
## Number only contain digits. (ok)
# arithmetic_arranger(["ss + 698", "380 - 2", "45 + 43", "123 + 49"],True)
## Numbers cannot be more than four digits. (ok)
# arithmetic_arranger(["32 + 698", "553801 - 2", "45 + 43", "123 + 49"],True)
# arithmetic_arranger(["32 + 698", "2 - 553801", "45 + 43", "123 + 49"],True)