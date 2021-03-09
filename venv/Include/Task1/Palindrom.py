num = input()

a = num[0:(len(num)+1)]
b = num[::-1]
print(a)
print(b)
if a == b:
    print('yes')
else:
    print('NOOOO')