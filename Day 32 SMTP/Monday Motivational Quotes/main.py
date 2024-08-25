#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com" # Put your email here
MY_PASSWORD = "abcd1234()" # Put your app password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("/Udemy/100 Days of Python/Day 32 SMTP/Monday Motivational Quotes/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

