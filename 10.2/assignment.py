# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# name = input("Enter file:")
name = "mbox-short.txt"

handle = open(name)
hours_and_times = dict()

for line in handle:
    if not "From " in line:
        continue
    date = line.rstrip().split(":")[0]
    hour = date[-2:]

    hours_and_times[hour] = hours_and_times.get(hour, 0) + 1

[print(hour + " " + str(times))
 for hour, times in sorted(hours_and_times.items())]
