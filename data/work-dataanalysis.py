# Data Analysis
# Author: Layla Ibrahim
#

# Analyse the data provided in class

def main():
#---- open the file ------
f = open ("central_park_weather.csv" , "r")

lines = f.readlines ()

# close the file BEFORE finishing
f.close()
lines = lines[1:]

# count data points
total = len(lines)
print("Total data points:", total)

# variables for averages
rain_sum = 0
rain_count = 0
tmin_sum = 0
tmin_count = 0

june_tmax_sum = 0
june_tmax_count = 0

# Go through each line
for line in lines:
    row = line.strip().split(",")

    date = row[0]
    precip = [1]
    tmin = row[4]
    tmax = row[5]

# rainfall
if precip == "":
    rain_sum += float(precip)
    rain_count += 1

#  minimum temperture
if tmin == "":
    tmin_sum += float(tmax)
    tmin_count +=
