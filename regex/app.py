import re
text = """
Ivan Ivanov
Age: 25 years
Phone: +7 (123) 456-7890
Email: ivanov@mail.ru

Maria Petrova
Age: 30 years
Phone: +7 (987) 654-3210
Email: petrova@mail.ru
"""

phone_regex = re.compile(r'\+\d \(\d{3}\) \d{3}-\d{4}')
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

phone = phone_regex.findall(text)
email = email_regex.findall(text)

print("Найденные номера телефонов:")
for phone_number in phone:
    print(phone_number)

print("\nНайденные почты:")
for email_address in email:
    print(email_address)
