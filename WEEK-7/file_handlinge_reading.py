'''
.txt
.xml
.json
.csv
.tsv
.xls
.yaml

'''

""" word_store = []
f = open('./sample.txt')
lines = f.read().splitlines()
for line in lines:
    words = line.replace('.', '').lower().split()
    word_store.extend(words)
f.close()
print(word_store) """

word_store = []
with open('./sample.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        words = line.replace('.', '').lower().split()
        word_store.extend(words)
    print(word_store)
    