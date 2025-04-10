import random
import datetime as dt
import smtplib

#================== LOGIN DETAILS ===================#
MY_EMAIL = "nompi@gmail.com"
My_PASSWORD = "abcdef1234*"

#----------------------- DATE AND TIME -----------------------#
now = dt.datetime.now()
weekdays = now.weekday() #Monday = 0, Tuesday = 1, Wednesday = 3 etc.

#-------------------------------------------------------------#
def sent_motivational_mail(weekday):
    with open("quotes.txt", "r") as file:
        all_quotes = file.readlines()
        #print(all_quotes)
        random_quotes = random.choice(all_quotes)

        #print(f"{weekday} {random_quotes}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, My_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = "nompi@outlook.com",
            msg = f"Subject:{weekday} Motivation\n\n{random_quotes}"
        )

Week_day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
for (week_day_no, week_day)  in Week_day.items():
    #print(week_day_no)
    if week_day_no == weekdays:
        sent_motivational_mail(week_day)
    else:
        pass
