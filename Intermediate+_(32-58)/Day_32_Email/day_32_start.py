import smtplib

#Put email and password
my_email = "...@gmail.com"
password = ""
#SMTP connection will vary depending on  email provider
# connection = smtplib.SMTP("smtp.gmail.com")

# my_email = "...@ghotmail.com"
# connection = smtplib.SMTP("smtp.live.com")

# my_email = "...@yahoo.com"
# connection = smtplib.SMTP("smtp.mail.yahoo.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    #Secure/encrypts connection
    connection.starttls()
    #Login to email
    connection.loggin(user=my_email, password= password)
    #Specify receiver and Message
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="", 
        msg="Subject:Hello\n\nThis is the body of my email."
    )
#End connection. Don't need to use if use with keyword
# connection.close()

""" Email will probably require extra steps to work
Find "App password" option
Select "Other" from dropdown list and enter an app name, then click Generate.
Copy the password and use this password in the code
"""

#Rename datetime module as dt to avoid confusion (datetime.datetime)
import datetime as dt
#Current date and time according to computer. datatime object data type
now = dt.datetime.now()
#Taps into year as int datatype
year = now.year

month = now.month
day_of_the_week = now.weekday()
#After day, default values are used
date_of_birth = dt.datetime(year=2020, month=2, day=13, hour=5)