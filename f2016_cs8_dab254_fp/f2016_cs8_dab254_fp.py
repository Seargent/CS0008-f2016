#
# Template for code submission
#
# name  :Davyd
# email :dab254@pitt.edu
# date  :14.12.16
# class :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# The code for the Final Project
#
# Notes:
# Well, I just took the template you gave us on the Blackboard and added the last part to show the distance run and
# runs for all the participants as individuals. I don't know if that what you wanted us to do, but it answered all the
# points of the Final Project, so  thought it is fine. It was a pleasure to study under you and hope to see you again,
# Max! Best wishes, Davyd...
#
# START OF THE PROGRAMME AND ITS COMMENTARIES!!!
#
# Class participant definition according to specs from header
#
# Defining a class
class participant:

    """Participant class"""
    # Name of the participant
    name = "unknown"
    # Total distance run by the participant
    distance = 0
    # Total number of runs by the participant
    runs = 0

    # Initializer methods
    def __init__(self, name, distance=0):
        # Setting name
        self.name = name
        # Setting distance if it is non-zero
        if distance > 0:
            # Setting distance
            self.distance = distance
            # Setting number of runs accordingly
            self.runs = 1

    # End def __init__

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1

    # End def addDistance

    # addDistances method
    def addDistances(self, distances):
        # Looping over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1

    # End def addDistance

    # Returning the name of the participant
    def getName(self):
        return self.name

    # End def getName

    # Returning the total distance run computed
    def getDistance(self):
        return self.distance

    # End def getDistance

    # Returning the number of runs
    def getRuns(self):
        return self.runs

    # End def getRuns

    # Stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

        # End def __init__

    # Converting to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

    # End def tocsv

# End class participant

def getDataFromFile(file):
    # Initializing output list
    output = []
    # Reading file line by line
    for line in open(file,'r'):
        # Excluding first line that is the header
        if "distance" in line:
            # Skipping line
            continue
        # Removing \n ending the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # Using try/except to avoid unhandled errors
        try:
            # Appending record to output list in the form of a dictionary with 2 keys: name and distance
            # Remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            # Catching all the lines that are incorrectly formatted and skipping them too
            print('Invalid row : '+line.rstrip('\n'))
    # Returning data records
    return output

# End def getDataFromFile

#
# Asking for master file from user
masterFile = input("Please, provide the master file: ")

# Reading the master file and extract data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)
#
rawData = sum([getDataFromFile(file) for file in dataFiles],[])
#
# Number of files read (this is equivalent to the number of elements in dataFiles)
numberFiles = len(dataFiles)
#
# Total number of lines read (this is equivalent to the sum of the second item in each item of rawData)
totalLines = len(rawData)
#
# Total number distance run by every participant (this is equivalent of the sum of the "distance" element of the items
# in the uniqueListdata)
totalDistanceRun = sum([item['distance'] for item in rawData])
#
participants = {}
# Looping on all the records
for item in rawData:
    # Checking if the names has already been found previously or if it is new (if it is new, initialize elements in the
    # accumulators)
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # Inserting distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])
#
# Initializing accumulators
# Minimum distance run with name
minDistance = { 'name' : None, 'distance': None }
# Maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# Appearences dictionary
apparences = {}
#
# Computing the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # Getting the total distance run by this participant
    distance = object.getDistance()
    # Checking if we need to update min (if this is the first iteration or if the current participant distance is lower
    # than the current min)
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # Checking if we need to update max (if this is the first iteration or if the current participant distance is lower
    # than the current min)
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance
    #
    # Getting number of runs, aka appearances from participant object
    participantAppearences = object.getRuns()
    #
    # Checking if we need to initialize this entry
    if not participantAppearences in apparences.keys():
        apparences[participantAppearences] = []
    apparences[participantAppearences].append(name)
#
# Computing total number of participant (this is equivalent to the length of the participantDistances)
totalNumberOfParticipant = len(participants);
#
# Compute total number of participants with more than one record
# Extract all the participants that have 2 or more runs and count the number of elements in the list with len()
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])
#
# Setting format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'
#
# Providing requested output
print("")
print(" Number of Input files read   : " + format(numberFiles,INTEGER))
print(" Total number of lines read   : " + format(totalLines,INTEGER))
print("")
print(" Total distance run           : " + format(totalDistanceRun,FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))
print("")
print(" Total number of participants : " + format(totalNumberOfParticipant,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,FLOAT))
print("")

for i in participants.keys():
    print(participants[i])
#
# Creating output file
outputFile = "f2016_cs8_dab254_fp.run.csv"
# Opening file for writing
fh = open(outputFile,'w')
# Writing header in file
fh.write('name,records,distance\n')
# Looping on all the participants
for name, object in participants.items():
    # Writing line in file
    fh.write(object.tocsv() + '\n')
# Closing files
fh.close()
