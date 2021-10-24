lis = ['32 + 50']

sprt = ' '.join(lis)  # split the list into string
a = sprt.rsplit()  # split the string into list

print(type(sprt))
	
print(sprt)

print(a)

print(type(a))

total = int(a[0]) + int(a[2])
print(total)
