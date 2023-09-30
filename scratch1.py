answer = True #False
data = [(3, 1, 2, '+'), (11, 5, 6, '+'), (1, 2, 1, '-'),(2, 4, 2, '-')]
nwtprnt = []

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
        nwtprnt.append(frmt)
        # print(frmt)
    else:
        nwtprnt.append(frmt2)
        # print(frmt2)

print(nwtprnt)

# arranged_problems = ''
# # print("-"*4)
# top_row = '1112   3222'
# bottom_row = '1 2'
# dashes = "---- - "
# dashes = dashes + "---- +"
# solutions = f'1{" "*4}5'
# arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
#
# print(arranged_problems)