import smtplib

my_email = "nomprster@gmail.com"
password = "ABCD1234*"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr= my_email,
        to_addrs= "nompi@outlook.com",
        msg= "Subject:Testing\n\nThis is the body of my email for testing."
    )