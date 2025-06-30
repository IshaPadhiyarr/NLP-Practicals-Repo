import re

text = "Order ID: 123456, Reference: 9876"
#Match at the beginning
match_result = re.search(r'Reference: \d+', text)
print("Match:" , match_result.group() if match_result else "No match")

#Find all number
numbers = re.findall(r'\d+', text)
print("Find All", numbers)

#Replace digit with 'X'
text = "My phone number is 98765-432102-03 and office number is 99887-665547"

#Masking phone numbers
masked_text = re.sub(r'\d{5}', 'XXXXX', text)
print("Masked text",masked_text)

import re

text = "My phone number is 98765-43210-02 and office number is 99887-66554-99"

# Match and mask the last 2 digits of the 3rd part
masked_text = re.sub(r'(\d{5}-\d{5}-)\d{2}', r'\1XX', text)

print("Masked text:", masked_text)

import re

text = "My phone number is 98765-43210-02 and office number is 99887-66554-99"

# Match and mask the 2nd part (middle 5 digits)
masked_text = re.sub(r'(\d{5}-)\d{5}(-\d{2})', r'\1XXXXX\2', text)

print("Masked text:", masked_text)

import re
text = "Contact us at support@email.com or sales@company.in"
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Extracted Emails:", emails)

