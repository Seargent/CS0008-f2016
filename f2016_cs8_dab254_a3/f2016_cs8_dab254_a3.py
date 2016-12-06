#
# Template for code submission
#
# name  :Davyd
# email :dab254@pitt.edu
# date  :20.11.16
# class :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# The code for Assignment 3
#
# Notes:
# MN: I think you should have created a file where storing the list of names, number of records and total distance run
#
# START OF THE PROGRAMME AND ITS COMMENTARIES!!!
#
# Importing collections module
import collections

# Declaring function named sumData, which will sum the distances for each participant
def sumData(data):
    # Creating new defaultdict object and store it in result
    result = collections.defaultdict(int)
    # Creating a count-controlled loop (for each element in data)
    for element in data:
        # Sorting the values for element in tuple (name,distance)
        name, distance = element
        # Updating the distance
        result[name] += distance
    # Creating the list form the result object
    return  [[i, total] for i, total in result.items()]

# Opening master file, reading it, splitting by delimiter \n, storing the result in files
# MN: why did you hard code the file name?
files=open("f2016_cs8_a3.data.txt").read().split("\n")
# Creating empty data list
data=[]
# Looping from 0 till len(files)-1
# MN: why not using: for file in files?
for i in range(0,len(files)-1):
    # Opening each data file, reading it, splitting by delimiter \n, storing in local veriable dataSource
    dataSource = open(files[i]).read().split("\n")
    # Looping from 1 till len(dataSource-1)
    for i in range(1, len(dataSource) - 1):
        # Splitting each entry in dataSource by delimiter "  ,", appending the result to the data list
        data.append(dataSource[i].split('  ,'))

# For each [name,distance] in data casting the distance to float, storing the new pair in data
data = [[i[0], float(i[1])] for i in data]

# Printing the number of files read
print("Number of files:\t%d"%(len(files)-1))

# Printing the number of line read, the number of lines is the number of lines in data + the number of
#  headers that was skipped
print("Number of lines:\t%d"%(len(data)+len(files)-1))
# Printing the total distance which is the sum of all distances in data
print("Total distance:\t%f"%(sum(i[1] for i in data)))
# Creating a count-controlled loop (for each element in the list which was returned by the sumData function)
for i in sumData(data):
    # Printing the name and the total distance
    print("Total distance for:\t%s is:\t %f"%(i[0],i[1]))

# MN: you should have compute min and max distance on the participant total distance
#     and not on the single record
#
# Finding the pair[name,distance] with the highest distance, storing the result in maxDist
maxDist=max(data,key=lambda x: x[1])
# Finding the pair[name,distance] with the smallest distance, storing the result in maxDist
minDist = min(data, key=lambda x: x[1])
# Printing the the pair[name,distance] from the maxDist
print("Max distance:\t%f by:\t%s"%(maxDist[1],maxDist[0]))
# Printing the the pair[name,distance] from the minDist
print("Min distance:\t%f by:\t%s" % (minDist[1], minDist[0]))

# Creating the list of names from the data, storing the result in names
names = [i[0] for i in data]
# Creating the set from names to remove the duplicates, printing the number of partisipants which is the lenght
#  of the set(names)
print("Total number of participants:\t%d"%len(set(names)))
# Finding the pairs[name,distance] with the number of occurrences > 1, storing the result in data
duplicates=[[i,names.count(i)] for i in names if names.count(i)>1]
# Creating a count-controlled loop (for each pair[name,distance] in duplicates printing the name and the distance)
for i in duplicates:
    # Printing the name and the distance
    print("%s %d"%(i[0],i[1]))
