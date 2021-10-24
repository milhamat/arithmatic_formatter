def arithmetic_arranger(problems):
    arranged_problems = []

    for datas in problems:
        data = datas.split()
        arranged_problems.append(data)

    print(arranged_problems)
    # return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])