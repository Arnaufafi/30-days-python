# Day 16 - 30DaysOfPython Challenge

from datetime import date, datetime

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formated_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formated_date)

# Today is 5 December, 2019. Change this time string to time
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object = ", date_object)

# Calculate the time difference between now and new year.
today = date(year=year, month=month, day=day)
new_year = date(year=year+1, month=1, day=1)
time_to_new_year = new_year - today

print(f"Difference between now and new year = {time_to_new_year}")

# Calculate the time difference between 1 January 1970 and now.
past_date = date(year=1970, month=1, day=1)
diff_since_1970 = today - past_date

print(f"Time difference between 1 January 1970 and now = {diff_since_1970}")