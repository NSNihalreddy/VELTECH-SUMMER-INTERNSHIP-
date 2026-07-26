import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

print("EMAIL:", repr(EMAIL))
print("PASSWORD LENGTH:", len(PASSWORD))

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL, PASSWORD)
        print("Login Successful!")
except Exception as e:
    print(type(e).__name__)
    print(e)