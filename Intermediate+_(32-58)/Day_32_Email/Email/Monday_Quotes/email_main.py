import smtplib, datetime as dt, random

MY_EMAIL =  "@gmail.com"
MY_PASSWORD = ""
#Datetime object for current time
now = dt.datetime.now()
#Get the day of the week
day_of_the_week = now.weekday()
#Check if the day of the week is Monday (0)
if day_of_the_week == 0:
    #Get quote data and put in a list
    with open("./Day_32_Email/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt") as file:
        message_list = file.readlines()
        email_body = random.choice(message_list)
    
    #Send Email
    with smtplib.STMP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addr= MY_EMAIL,
            msg=f"Subject:Monday Quote\n\n{email_body}"
        )