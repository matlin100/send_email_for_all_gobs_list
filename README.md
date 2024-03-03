# Project Title
this script send message to a list of emails, created for send emails to tils of jubs recruiting

## Features
- send message to a list of emails
- filter legally emails
- send message to a list of emails

## Installation
make sore you have installed python 3 and latest on your PC

clone / fork the repository 
run git clone https://github.com/matlin100/send_email_for_all_gobs_list.git

run pip install python-dotenv email-validator


## setup 
create an .env file for stot your email and password 
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=yourapppassword

### Steps Password
1. **Navigate to Google Security Settings**
   - Access your Google Account security settings by visiting [Google Security Settings](https://myaccount.google.com/security).
2. **Enable 2-Step Verification**
   - If not already enabled, turn on 2-Step Verification to add an additional layer of security to your account.
3. **Generate a New App Password**
   - Return to the Security page, scroll down to find the “App passwords” section, and generate a new password. This is necessary if you are using 2-Step Verification.
4. **Update Your .env File**
   - Insert the generated password into your .env file under the variable `GMAIL_APP_PASSWORD`.

### setup email list
crate in ./data file data.json > ./data/data.json
in data.json put your email list in this structure
[
    {"emailAddress": "8300142@gmail.com"},
    {"emailAddress": "8300142@gmail.com"},
    {.......}...

### add cv pdf to email 
if you what to send CV pdf file >
add your SV to the ./data folder and rename it to CV.pdf > ./data/CV.pdf
## run
run the main file and it will send the emails to all
it will print the list of successful emails 
and unsuccessful emails 



