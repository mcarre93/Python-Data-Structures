# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the hour
# out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.
dic = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
# For each line in the file
for line in handle:
    # If the line starts with 'From '
    if line.startswith("From "):
        # Split the line into a list of words called linelist
        linelist = line.split()
        # Index the fifth place in the list as we know the time is stored there
        time = linelist[5]
        # Further split the time string by where the colons are placed and pull
        # out the first index as we know that the first index represents the hour
        hour = time.split(':')[0]
        # If the hour is in dic, increment by one. Otherwise, the default value for
        # the hour will be 0
        dic[hour] = dic.get(hour,0) + 1

# Convert dic into a list of tuple so that it may be sorted by key
tuple_list = list(dic.items())
tuple_list.sort()
for key,value in tuple_list:
    print (key,value)
