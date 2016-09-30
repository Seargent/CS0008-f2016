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
u = "USC"
m = "Metric"
inp_1 = input("Please, choose either USC(u) or Metric(m) system:")
inp_2 = float(input("Please, enter the total distance driven:"))
inp_3 = float(input("Please, enter the total gasoline spent:"))
#
if (inp_1 == "u"):
    kpm = round(inp_2 * 1.60934, 3)
    lpg = round(inp_3 * 3.78541, 3)
    Lp100Km = round((100 * lpg)/kpm, 3)
    mpg = round(inp_2/inp_3, 3)
elif (inp_1 == "m"):
    mpk = round(inp_2 * 0.621371, .3)
    gpl = round(inp_3 * 0.264172, 3)
    mpg = round(mpk/gpl, 3)
    Lp100Km = round((100 * inp_3)/inp_2, 3)
else:
    print("Error, wrong system given!")
#
if (Lp100Km > 20):
    n = "Gas consumption rating: Extremely poor"
elif (Lp100Km <= 20 and Lp100Km > 15):
    n = "Gas consumption rating: Poor"
elif (Lp100Km <= 15 and Lp100Km > 10):
    n = "Gas consumption rating: Average"
elif (Lp100Km <= 10 and Lp100Km > 8):
    n = "Gas consumption rating: Good"
elif (Lp100Km <= 8):
    n = "Gas consumption rating: Excellent"
#
print("{:>34}        {:^1}".format("USC", "Metric"))
print("{0}    {1} {2}   {3} {4}".format("Distance ______________:", inp_2 if inp_1 == "u" else mpk, "miles", \
                                   inp_2 if inp_1 == "m" else kpm, "Km"))
print("{0}    {1} {2}   {3} {4}".format("Gas ___________________:", inp_3 if inp_1 == "u" else gpl, "gallons", \
                                   inp_2 if inp_1 == "m" else lpg, "Liters"))
print("{0}    {1} {2}   {3} {4}".format("Consumption ___________:", mpg, "mpg", Lp100Km, "L/100Km"))
print(n)
#