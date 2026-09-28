#Step1: Import the regular expression module
import re

#Step2: Store the text in a variable
text = """
Hello students!
For any queries, contact abc@gmail.com or teachr123@college.edu
You can also contact support@yahoo.com
"""
email_pattern = r'[a-zA-Z0-9,_%+-]+@[a-zA-Z0-9,-]+\,[a-zA-Z]{2,}'

#Step4: Find all email addresses in the text
emails = re.findall(email_pattern, text)

#Step5: Display a heading
print("Email addresses found. ")

#Step6: Display each email addresses
for email in emails:
    print(email)
