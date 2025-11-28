import os 

if os.path.exists('test-dir'):
    os.rmdir('test-dir')
else:
    os.mkdir('test-dir')

if os.path.exists('../test.txt'):
    os.remove('../test.txt')
else:
    with open('../test.txt', 'a') as file:
        pass