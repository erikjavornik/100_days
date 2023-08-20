##################### Normal Starting Project ######################
import smtplib, datetime as dt, random, pandas
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)/Day_32_Email/Birthday_Wish/birthday-wisher-normal-start/letter_templates/
now = dt.datetime.now()
today = (now.month, now.day)

# HINT 2: Use pandas to read the birthdays.csv
df = pandas.read_csv("./Day_32_Email/Birthday_Wish/birthday_data.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24/Day_32_Email/Birthday_Wish/birthday-wisher-normal-start/letter_templates/
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
birthday_dict = {(row.month,row.day):row for (index, row) in df.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
if today in birthday_dict:
    rand_letter = random.randint(1,3)
    person_name = birthday_dict[today]["name"]
    print(person_name)
    with open(f"./Day_32_Email/Birthday_Wish/letter_temp/letter_{rand_letter}.txt") as file:
        letter = file.read()
        named_letter = letter.replace("[NAME]", person_name)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
    my_email = "...@gmail.com"
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.loggin(user=my_email, password= password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_dict[today]["email"], 
            msg=f"Subject:Happy Birthday\n\n{named_letter}"
        )