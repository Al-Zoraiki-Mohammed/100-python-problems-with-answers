n= input('enter number of elements: ')
t= tuple([ int(i) for i in (input(f'enter {n} values separated by space:').split())])
print(hash(t))

