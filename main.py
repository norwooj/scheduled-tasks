import random as rnd
import smtplib
import pandas as pd
import datetime as dt
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
today = dt.datetime.now()
month = today.month
day = today.day
birthdays = pd.read_csv('birthdays.csv')
birthdays = birthdays.to_dict('records')
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for birthday in birthdays:
    if birthday["day"] == day and birthday["month"] == month:
        chosen_letter = rnd.choice(letters)
        with open(f"letter_templates/{chosen_letter}", "r") as file:
            chosen_letter = file.read()
        chosen_letter = chosen_letter.replace("[NAME]", birthday["name"])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday["email"],
                                msg=f"Subject:Happy Birthday!\n\n{chosen_letter}")



