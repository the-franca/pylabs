import os
os.system('clear')

num = int(input('Enter a number: '))

print(f'Multiplication table of {num}')
for i in range(1, 11):
    res = num * i
    print(f'{num} x {i} = {res}')