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