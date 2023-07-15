## Birthday Mailer

### Description
Automate birthday emails to friends,
in every language.

This project is written in Python

### Resources And Libraries
- Pandas
- SMTP (email sending library)
- Datetime
- email.message (encode and decode, utf-8)

## Instructions

1. Create a file called '/data/env_verbs.py' 
    for security
    with your email and password (generated from your account for your app):
    ```commandline
    PASSWORD = "dfgjkdgsd"
    MY_EMAIL = "myaccount@gmail.com"
    ```

2. Create a file called '/data/friend_birthdays.csv' and save all your friends data there.

    it will contain a name, birthdate and email and should look like this:
    ```commandline
    Name,Birthday,Email
    Amit,1989-3-29,amitaccount@gmail.com
    Tomer,1996-10-1,tomeraccount@gmail.com
    ```


3. Create a custom plate of a birthday greet file called
'/letters/birthday_greet.txt' that looks something like this:
    ```commandline
    Happy Birthdy [name]!
    
    You turnd [age] and that is no joke..
    I wish you the best,
    
    my_name
    ```
    The [name] and [age] will be replaced with the friend's details by the generate_birthday_greet function in the 'main.py' file.     
