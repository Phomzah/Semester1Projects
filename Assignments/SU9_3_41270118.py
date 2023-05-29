#41270118 Phomolo Legobye

# This program asks the user to enter an email address,
# loops through the characters in the email address,
# and prints out Output

# Input
email = input("Enter an email address: ")

# Find the position of the "@" symbol
at_index = email.find("@")

# Extract the name and domain using slicing
name = email[:at_index]
domain = email[at_index + 1:]

# Output
print("\nName:", name)
print("Domain:", domain)
