
with open('nots.txt', 'w') as f:
    for i in range(101):
        f.write(f'{i} x {i} = { i ** 2}\n')
