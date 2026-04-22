import datetime
import pytz  
# pytz:
# - Provides a large list of timezones
# - Common practice: store and work in UTC, convert to local time only when needed


# -------------------- Creating Timezone-aware Datetime --------------------

dt = datetime.datetime(2026, 4, 22, 10, 52, 40, tzinfo=pytz.UTC)
# Creates a timezone-aware datetime in UTC
print(dt)


# -------------------- Current Time (UTC) --------------------

dt_now = datetime.datetime.now(tz=pytz.UTC)
# Recommended way → returns current time with UTC timezone
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# Older approach:
# utcnow() returns naive datetime → manually attach UTC timezone
print(dt_utcnow)


# -------------------- Timezone Conversion --------------------

dt_mytz = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))
# Converts UTC time → IST (Asia/Kolkata)
print(dt_mytz)


# -------------------- List All Timezones --------------------

for tz in pytz.all_timezones:
    print(tz)
# Prints all available timezone names in pytz


# -------------------- Naive → Aware Conversion --------------------

dt_nv = datetime.datetime.now()
# Naive datetime (no timezone info)

mtz = pytz.timezone('Asia/Kolkata')
# Define target timezone

dt_nv = mtz.localize(dt_nv)
# Convert naive → timezone-aware datetime (correct method in pytz)
print(dt_nv)


# -------------------- Formatting Datetime --------------------

print(dt_mytz.isoformat())
# ISO 8601 format (standard for APIs, logs)

print(dt_mytz.strftime('%B %d , %Y'))
# Custom string formatting (Month Day, Year)


# -------------------- String → Datetime --------------------

dt_str = 'April 22 , 2026'
dt1 = datetime.datetime.strptime(dt_str, '%B %d , %Y')
# Parses string → datetime object
print(dt1)


# -------------------- Key Concepts --------------------

# strftime → Datetime → String
# strptime → String → Datetime
