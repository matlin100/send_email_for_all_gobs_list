# Project Title
this script send message to a list of emails, created for send emails to tils of jubs recruiting

## Features
- send message to a list of emails
- filter legally emails
- send message to a list of emails

## Installation
make sore you have installed python 3 and latest on your PC

clon / fork the repository 

run pip install python-dotenv
run pip install email-validator

## Usage
create an .env file for stot your email and password 
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=yourapppassword

sometimes you will need to create a special password key for Third party applications on google security and pass the password key that provided by google to the .env password 
navigating to https://myaccount.google.com/security.>Enable 2-Step Verification (if you haven’t already):>back to the security page (https://myaccount.google.com/security).>Scroll down to the “Signing in to Google” section.>
Find “App passwords” and click on it.> and set a new password 


crate in ./data file data.json > ./data/data.json
in data.json put your email list in this structure
[
    {"emailAddress": "8300142@gmail.com"},
    {"emailAddress": "8300142@gmail.com"},
    {.......}...
[

if you what to send CV pdf file >
add your SV to the ./data folder and rename it to CV.pdf > ./data/CV.pdf
## Contributing
run the main file and it will send the emails to all
it will print the list of successful emails 
and unsuccessful emails 

## License
Your project’s license. Common licenses include MIT, GPL, and Apache.
