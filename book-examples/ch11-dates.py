from datetime import date, datetime, time

#p.305 basic date stuff
date_today = date.today()
print(f"date_today: {date_today}")
datetime_today = datetime.today()
print(f"date_today: {datetime_today}")
datetime_now = datetime.now()
print(f"date_now: {datetime_now}")
time_now = datetime_now.time()
print(f"time_now: {time_now}")

christmas = date(2024,12,25)
print(f"christmas: {christmas}")
time_eleven = time(11,11,11)
print(f"time_eleven: {time_eleven}")

#p.307 datetime parsing strings
christmas_date_str = "12/25/24"
halloween_date_str = "2024-10-31"
appointment_date_time_str = "2024-05-09 08:00"

christmas_date = datetime.strptime(christmas_date_str, '%m/%d/%y')
print(f"christmas_date_str: {christmas_date}")
halloween_date = datetime.strptime(halloween_date_str, '%Y-%m-%d')
print(f"halloween_date_str: {halloween_date}")
appointment_date = datetime.strptime(appointment_date_time_str, '%Y-%m-%d %H:%M')
print(f"appointment_date_time_str: {appointment_date}")

#p.309 - formatting dates
christmas_date_formatted = christmas_date.strftime("%m/%d/%y")
print(f"christmas_date_formatted: {christmas_date_formatted}")
halloween_date_formatted = halloween_date.strftime("%Y-%m-%d")
print(f"halloween_date_str: {halloween_date_formatted}")
appointment_date_formatted = appointment_date.strftime("%Y-%m-%d %H:%M")
print(f"appointment_date_formatted: {appointment_date_formatted}")

# from book - double checking syntax that didn't work for me
# I was missing the f string, converting to string.
halloween = datetime(1988, 10, 31, 22, 48)
halloween_date_formatted = f"{halloween:%Y-%m-%d}"
print(f"{halloween_date_formatted}")

# spans of time
from datetime import timedelta
print("--- timedeltas ---")
three_weeks = timedelta(weeks=3)
print(f"Three weeks from today: {date_today + three_weeks}")
print(f"Three weeks ago today: {date_today - three_weeks}")
time_span_until_christmas = christmas - date_today
print(f"Time Span until christmas: {time_span_until_christmas}")
print(f"Days until christmas: {time_span_until_christmas.days}")