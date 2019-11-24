# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# name = input("Enter file:")
name = "mbox-short.txt"

people = {}
all_text = open(name).read()

for from_line in all_text.split("From "):
    from_list = from_line.split()
    if len(from_list) < 1:
        continue
    email = from_list[0]
    people[email] = people.get(email, 0) + 1

maximum = 0
greatest_emailer = ""
for person, number_of_emails in people.items():
    if number_of_emails < maximum:
        continue
    maximum = number_of_emails
    greatest_emailer = person

print(greatest_emailer, maximum)
