def arithmetic_arranger(problems):
    # first format the list data input
    new_list = [problems[i:i + 1] for i in range(0, len(problems), 1)]
    print(new_list)






arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])