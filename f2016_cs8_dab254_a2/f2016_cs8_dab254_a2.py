#
# Template for code submission
#
# name  :Davyd
# email :dab254@pitt.edu
# date  :27.10.2016
# class :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# The code for Assignment 2
#
# Notes:
# Help, I need somebody Help, not just anybody
#
# START OF THE PROGRAMME AND ITS COMMENTARIES!!!
#
# Function(or Method as it doesn't return any value back) #1:
# Making function for printKV
def printKV(key, value, klen = 0):
    # Finding the total key length
    kl = len(key)
    space = klen
    # Getting maximum space
    if (kl>klen):
        space = kl
    #Checking if value is an int
    if (isinstance(value, int)):
        # Printing int value and our pre-made string
        print('%-20s: %-10d' % (key, value))
    # Otherwise
    else:
        # Printing float number and our pre-made string
        print('%-20s: %-10.3f' % (key, value))
#
# Function #2:
# Reading from file FO
def processFile(FO):
    # Total number of lines counter
    line_count = 0
    # Total distance run counter
    sum_total = 0
    # Opening file
    fp = open(FO, 'r')
    # For all lines in FO
    for line in fp:
        # Increasing line count
        line_count += 1
        # Removing '\n'(new line) from the end of each line
        line = line.rstrip()
        # Splitting string and float to create a list
        st = line.split(',')
        # Finding sum_total
        sum_total += float(st[1])
    # returning data
    return line_count, sum_total
#
# Total sum (number of lines) of all files
whole_line = 0
# Total sum (distance run) of all files
whole_sum = 0
#
# Making infinite loop (as we don't know the number of files which user will put in the programme)
while(True):
    # Making a void line for beautification sake
    print(' ')
    # Getting file name (remember that files should be in repository in order for them to be used):
    FO = input('Please, enter file to be read:')
    # Checking if user wants to quit, as we don't know how many files was used
    if ((FO=='quit') or (FO=='q')):
        # Ending the infinite loop
        break
    # Processing the file:
    line_count, sum_total = processFile(FO)
    # Printing partial total sum of lines and partial distance run
    printKV('Partial Total # of lines', line_count)
    printKV('Partial distance run', sum_total)
    whole_line += line_count
    whole_sum += sum_total
#
# Making a void line for beautification sake
print(' ')
# Printing total sum of lines and total distance run
print('Totals:')
printKV('Total # of lines', whole_line)
printKV('Total distance run', whole_sum)