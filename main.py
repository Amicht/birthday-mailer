import smtplib
import pandas
import datetime as dt
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def send_email(title, content, email_address):
    message = EmailMessage()
    message['Subject'] = title
    message['From'] = MY_EMAIL
    message['To'] = email_address
    message.set_content(content)
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.send_message(message)
    except:
        print(f"Failed to send email to {email_address}")


def get_current_birthdays():
    '''Returns [ {name: str, age:int, email: str} ]'''
    data = pandas.read_csv("data/friends_birthdays.csv")
    names = data["Name"].to_list()
    emails = data["Email"]
    birthdays = [str_bd.split("-") for str_bd in data["Birthday"].to_list()]

    current_bds = [
        {
            "name": names[index],
            "email": emails[index],
            "age": dt.datetime.now().year - int(birthdays[index][0])}
        for index in range(len(birthdays) - 1)
        if dt.datetime.now().month == int(birthdays[index][1])
           and dt.datetime.now().strftime("%d") == birthdays[index][2]
    ]
    return current_bds


def generate_birthday_greet(name, age):
    with open('letters/birthday_greet.txt', encoding="utf8") as file:
        greed = file.read()

    return greed.replace("[name]", name).replace("[age]", age)


def send_birthday_emails():
    birthdays = get_current_birthdays()
    for bd in birthdays:
        name = bd.get("name")
        age = bd.get("age")
        email = bd.get("email")
        card = generate_birthday_greet(name, str(age))
        email_title = "יומולדת שמח!"
        send_email(title=email_title, content=card, email_address=email)
        print("send successfully")


send_birthday_emails()
