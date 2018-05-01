# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# the sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to
# a count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.

# Input file, read file into a list word by word, refine that list of words into
# another list that only consists of email addresses, then map the frequency of
# those senders into a dictionary.

senderlist = []
counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith("From "):
        linelist = line.split()
        sender = linelist[1]
        if sender in counts:
            counts[sender] = counts[sender] + 1
        else:
            counts[sender] =  1
                # More concise method of retrieving, creating, and updating
                # counts[sender] = counts.get(sender,0) + 1
    else:
        continue

# Using -1 as a flag in this case is acceptable because we are only dealing with
# positive values in finding the highest frequency email sender
largest = -1
prolific_sender = None
for key,value in counts.items():
    if value > largest:
        largest = value
        prolific_sender = key
print(prolific_sender, largest)
