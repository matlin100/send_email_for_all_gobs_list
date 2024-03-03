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

App Password Creation: Generate a unique password for third-party applications through your Google Security settings:
	•	Navigate to Google Security Settings.
	•	Enable 2-Step Verification (if not already enabled).
	•	Return to the Security page, find “App passwords”, and generate a new password.
	•	Insert the generated password into your .env file under GMAIL_APP_PASSWORD.
 

crate in ./data file data.json > ./data/data.json
in data.json put your email list in this structure
[
    {"emailAddress": "8300142@gmail.com"},
    {"emailAddress": "8300142@gmail.com"},
    {.......}...
[

if you what to send CV pdf file >
add your SV to the ./data folder and rename it to CV.pdf > ./data/CV.pdf
## run
run the main file and it will send the emails to all
it will print the list of successful emails 
and unsuccessful emails 



