from python_date_time import generate_date_time
import os

with open('log.txt','a') as f:
    time_stamp = generate_date_time('eu', 'long')
    f.write(f'Asab {time_stamp}\n')
    
    
if os.path.exists('./sample.txt'):
    os.remove('./sample.txt')
    
    
# JavaScript Object Notation => JSON 