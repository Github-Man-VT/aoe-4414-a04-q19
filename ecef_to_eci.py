## Script Name: ecef_to_eci.py

## Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km

## Parameters:
# year: Value for year(s)
# month: Value for month(s)
# day: Value for day(s)
# hour: Value for hour(s)
# minute: Value for minute(s)
# second: Value for second(s)
# ecef_x_km: X-Magnitude for ECEF Vector
# ecef_y_km: Y-Magnitude for ECEF Vector
# ecef_z_km: Z-Magnitude for ECEF Vector

## Output: Converts ECEF Vector into ECI Vector

## Written by Carl Hayden

## Importing Libraries
import math
import sys # argv
import numpy

## Defining Constants

## Initialize Script Arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')
ecef_x_km = float('nan')
ecef_y_km = float('nan')
ecef_z_km = float('nan')

## Parse Script Arguments
if len(sys.argv)==10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    ecef_x_km = float(sys.argv[7])
    ecef_y_km = float(sys.argv[8])
    ecef_z_km = float(sys.argv[9])

else:
    print(\
        'Usage: '\
        'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
    )
    exit()

## Main Script
JD = day - 32075 + 1461 * (year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12 - 3*((year+4900+(month-14)/12)/100)/4
JD_midnight = JD - 0.5
D_fractional = (second + 60 *(month+60*hour))/86400
JD_fractional = JD_midnight + D_fractional
T_UT1 = (JD - 2451545.0)/36525.0
wVal = 7.292115 * 10**(-5)
Theta_GMST = 67310.54841 + ((876600*60*60 + 8640184.812866) * T_UT1) + (0.093104 * T_UT1**2) + (-6.2*10**(-6) * T_UT1**3)

Extra_Rad_GMST = math.fmod(Theta_GMST, 360)*wVal
Rad_GMST = math.fmod(Theta_GMST*(2*math.pi/86400), (2*math.pi))-Extra_Rad_GMST

ECEF_Vect = numpy.array([[ecef_x_km], [ecef_y_km], [ecef_z_km]])

Rotation1 = numpy.array([[math.cos(-Rad_GMST), -math.sin(-Rad_GMST), 0], 
             [math.sin(-Rad_GMST), math.cos(-Rad_GMST), 0], 
             [0, 0, 1]])

Rotation1 = numpy.linalg.inv(Rotation1)

Calc1 = numpy.dot(Rotation1, ECEF_Vect)

eci_x_km = str(numpy.extract(1,Calc1[[0]]))
eci_y_km = str(numpy.extract(1,Calc1[[1]]))
eci_z_km = str(numpy.extract(1,Calc1[[2]]))

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)