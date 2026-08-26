import re

# Read the text file
with open("emails.txt", "r") as file:
    text = file.read()

# Find all email addresses
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

# Remove duplicate emails
emails = list(set(emails))

# Save extracted emails
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print(f"Total emails found: {len(emails)}")