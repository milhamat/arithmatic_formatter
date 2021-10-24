lis = ['32 + 50']

sprt = ' '.join(lis)  # split the list into string
a = sprt.rsplit()  # split the string into list

# print(type(sprt))  # debug the type of sprt

# print(sprt)  # debug the result of sprt

# print(a)  # debug the result of a

# print(type(a))  # debug the type of a

total = int(a[0]) + int(a[2])
print(total)
