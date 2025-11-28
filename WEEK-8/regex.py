import re 

txt = 'I Love is People'
pattern = 'love|hate'
match = re.match(pattern, txt, re.I)

if match:
    print('There is a match', match)
    print(match.span())
    start, end = match.span()
    print(start, end)
    print(txt[start:end])
else:
    print('There is no match')
    
    
txt = 'I love Python. There is not think like love . Love is the best thing in Python lesson.'

match = re.search(pattern, txt, re.I)
print(match)

matches = re.findall(pattern, txt, re.I)
print(matches)

if 'Hate' in matches:
    print('The text might have offensive statement')
else:
    print('The text is plain and safe to send it')
    
    

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

sentences = re.split(r'\n', txt)
print(len(sentences), sentences)


txt = '''%?#@#I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%?#@#%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ch%?#@#ing m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y@%o%u to b%e a t%e%a%che%?#@#r?'''

matches = re.sub(r'[^\w. ]', '', txt, re.I)
print(matches)
    
    