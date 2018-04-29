# 7.2 Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# when you are testing below enter mbox-short.txt as the file nameself.

fname = input('Enter file name: ')
fh = open(fname)

total = 0
count = 0
num = 0
index = 0

for lines in fh:
    if lines.startswith('X-DSPAM-Confidence:'):
        lines = lines.rstrip()
        count += 1
        index = (lines.find(':')) + 1
        # print(index)
        num = lines[index:]
        # print(num)
        num = float(num)
        #print(type(num))
        total = float(num + total)

average = total / count
print ("Average spam confidence:", average)
