import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
#print(day_of_week)

date_of_birth = dt.datetime(year=1986, month=5, day=25)
today = dt.datetime(year=2025, month=3, day=3)
dob = 14162/360
my_dob_year = str(round(dob, 2))
my_dob_year_splits = my_dob_year.split('.')
my_years = my_dob_year_splits[0]
my_days = my_dob_year_splits[1]
print(f"I am {my_years} Years and {my_days} days old.")
#print(today - date_of_birth)