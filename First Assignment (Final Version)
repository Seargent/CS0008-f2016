#
# Template for code submission
#
# name  :Davyd
# email :dab254@pitt.edu
# date  :29.09.16
# class :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# First Assignment (Task from the test)
#
# START OF THE PROGRAMME AND ITS COMMENTARIES!!!
#
# Assigning variables to our Metric Systems.
#
u = "USC"
m = "Metric"
#
# Assigning variables to user's input.
#
inp_1 = input("Please, choose either USC(u) or Metric(m) system:")
inp_2 = float(input("Please, enter the total distance driven:"))
inp_3 = float(input("Please, enter the total gasoline spent:"))
#
# First if-block in which programme calculate user's Miles per Gallons and Liters per 100 Kilometers.
# This will depend on which Metric System user decided to use.
# Also, if user was to put wrong Metric System, it will tell him about this.
#
if (inp_1 == "u"):
    kpm = inp_2 * 1.60934
    lpg = inp_3 * 3.78541
    Lp100Km = (100 * lpg)/kpm
    mpg = inp_2/inp_3
elif (inp_1 == "m"):
    mpk = inp_2 * 0.621371
    gpl = inp_3 * 0.264172
    mpg = mpk/gpl
    Lp100Km = (100 * inp_3)/inp_2
else:
    print("Error, wrong system given!")
#
# Second if-block in which programme takes values, calculated in first in-block, and compare it to the its data.
# It means that programme will compare in what range the fuel consumption lay and tell its rating to user.
# Both the range and the rating is data that was given to us and preset beforehand.
# It cannot be changed by user.
#
if (Lp100Km > 20):
    cm = "Gas consumption rating: Extremely poor"
elif (Lp100Km <= 20 and Lp100Km > 15):
    cm = "Gas consumption rating: Poor"
elif (Lp100Km <= 15 and Lp100Km > 10):
    cm = "Gas consumption rating: Average"
elif (Lp100Km <= 10 and Lp100Km > 8):
    cm = "Gas consumption rating: Good"
elif (Lp100Km <= 8):
    cm = "Gas consumption rating: Excellent"
#
# Last part of the programme in which it creates a table with our data.
# Data was calculated beforehand in our two if-blocks.
# It also gives Gas consumption rating underneath the table.
# Note that there is a blank line that separates the table from the data given and the Gas consumption rating.
# This lines were added for convenience.
#
print(" ")
print("{0:>42}{1:>22}".format("USC", "Metric"))
print("{0:>12} {1:>12,.3f}{2:>12} {3:>12,.3f}{4:>12}".format("Distance ______________:", inp_2 if inp_1 == "u" else mpk, \
                                                            "miles", inp_2 if inp_1 == "m" else kpm, "Km"))
print("{0:>12} {1:>12,.3f}{2:>12} {3:>12,.3f}{4:>12}".format("Gas ___________________:", inp_3 if inp_1 == "u" else gpl, \
                                                            "gallons", inp_2 if inp_1 == "m" else lpg, "Liters"))
print("{0:>12} {1:>12,.3f}{2:>12} {3:>12,.3f}{4:>12}".format("Consumption ___________:", mpg, "mpg", Lp100Km, "L/100Km"))
print(" ")
print(cm)
#
# END OF THE PROGRAMME AND ITS COMMENTARIES!!!
#