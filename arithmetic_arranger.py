def arithmetic_arranger(problems):
    arranged_problems = []
    result = []

    for datas in problems:
        data = datas.split()
        # data variable there is for splitting the list data into more separate list so it will return 3 nested list
        arranged_problems.append(data)

    print(arranged_problems)

    for i in arranged_problems:
        print(i)
    # return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])