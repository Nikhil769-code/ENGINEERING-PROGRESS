import datetime 

# -------------------- Date Basics --------------------

# Naive → no timezone info
# Aware → includes timezone (more accurate for real-world use)

d = datetime.date(2026, 4, 22)
# Creating a date object (year, month, day)
print(d)

tday = datetime.date.today()
# Current local date
print('{0.year} {0.day} {0.month}'.format(tday))
# Accessing year, day, month individually


# -------------------- Weekday Info --------------------

print(tday.weekday())  
# Monday = 0, Sunday = 6

print(tday.isoweekday())  
# Monday = 1, Sunday = 7


# -------------------- Timedelta (Date Arithmetic) --------------------

tdelta = datetime.timedelta(days=7)  
# Represents a duration of 7 days

print(tday + tdelta)  
# Date after 7 days

print(tday - tdelta)  
# Date 7 days ago

# Adding/subtracting timedelta → returns another date


bday = datetime.date(2027, 3, 30)

till_bday = bday - tday  
# Subtracting two dates → returns timedelta

print(till_bday)  
# Number of days remaining

print(till_bday.total_seconds())  
# Total seconds remaining


# -------------------- Time Object --------------------

t = datetime.time(9, 30, 30, 100000)  
# (hour, minute, second, microsecond)

print(t)
print(t.hour)


# -------------------- Datetime Object --------------------

dt = datetime.datetime(2026, 5, 22, 12, 33, 22, 100000)
# Combines both date and time

print(dt)
print(dt.date())  
# Extract date part

print(dt.time())  
# Extract time part

print(dt.hour)  
# Access individual attributes


# -------------------- Datetime Arithmetic --------------------

tdelta1 = datetime.timedelta(days=7, hours=12)
print(dt + tdelta1)  
# Adds both days and hours


# -------------------- Current Datetime Variants --------------------

dt_today = datetime.datetime.today()
# Local datetime (naive, no timezone info)

dt_now = datetime.datetime.now()
# Same as today(), but allows timezone argument

dt_utcnow = datetime.datetime.utcnow()
# Current UTC time (still naive, tzinfo=None)

print(dt_today)
print(dt_now)

# Difference:
# .today() → local time (naive)
# .now() → local time, can accept timezone

print(dt_utcnow)
# UTC time but still naive (no timezone attached)
