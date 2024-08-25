import smtplib

my_email = "example@gmail.com" # This is your existing email
password = "examplepassword" # You need to replace this with your App Password

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # tls: Transport Layer Security
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="example.reciever@yahoo.com",  # This is reciever existing email
                        msg="Subject: Write Anything\n\nThis is the body of my email")



"""
SMTP Email Provider
===================

For,
    Gmail = smtp.gmail.com
    Hotmail = smtp.live.com
    Yahoo = smtp.mail.yahoo.com

"""

# The email without subject will will go to your spam box.

"""
Steps to get the Gmail App Code
===============================

1. Go to your "Google Account"
2. Go to "Security"
3. Go to "2-step verification" and turn it on
4. After setting up your "2-step verification"
    Go to "App password":
        In the "select app" dropdown section select "Other" and name app as you want
        such as "exampleapp" and click generate.
        Finally copy your "app password"

### These steps are different for YAHOO & HOTMAIL ###

"""

