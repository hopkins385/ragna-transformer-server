import re

def hide_emails(text: str):
    # Simple regex to hide email addresses
    return re.sub(r'[\w\.-]+@[\w\.-]+', '<email>', text)

def hide_urls(text: str):
    # Simple regex to hide URLs
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '<url>', text)

def hide_phone_numbers(text: str):
    # Simple regex to hide phone numbers
    return re.sub(r'\+?[0-9\s\-\(\)]{7,}', '<phone>', text)