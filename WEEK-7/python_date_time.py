from datetime import datetime 

def generate_date_time(format ='EU', length = 'short'):
    now = datetime.now()
    year = now.year
    month = now.month 
    day = now.day
    hour = now.hour
    minute = now.minute 
    second = now.second
    if format.lower() == 'eu':
        if length == 'short':
            return f'{day}/{month}/{year}'
        else:
            return f'{day}/{month}/{year} {hour}:{minute}'
    elif format.lower() == 'us':
        if length == 'short':
            return f'{month}/{day}/{year}'
        else:
            return f'{month}/{day}/{year} {hour}:{minute}'
        

print(generate_date_time())
print(generate_date_time('US', 'long'))


new_year = datetime(2026, 1, 1)
last_year = datetime(2025, 1, 1)


now = datetime.now()
# print(now.strftime("%A %B %d, %Y %-I:%M %p"))

print(now.strftime('%A %B %d, %Y %I:%M %p'))

date_string = "5 December, 2019"
print(datetime.strptime(date_string, "%d %B, %Y"))

challenge_at_day_16 = datetime.strptime(date_string, "%d %B, %Y")
now = datetime.now()
time_elapsed = now - challenge_at_day_16
print(time_elapsed)
new_year = datetime(2026, 1, 1)
print(new_year - now)

# today = date(year=2019, month=12, day=5)
# new_year = date(year=2020, month=1, day=1)
# time_left_for_newyear = new_year - today



