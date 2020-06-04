# MCS 260, Project One, by Veronica Kalicki
import math

print("Hello, welcome to my range-of-projectile-subject-to-wind calculator!")
# introduction of variables
g = 9.80665
vx = input('Give initial horizontal velocity of the projectile: ') # intital horizontal velocity
vy = input('Give initial vertical velocity of the projectile: ') # initial vertical velocity
w = input('Give the wind velocity: ') # wind speed
y0 = input('Give initial height of the projectile above ground: ') # initial height


v = math.sqrt((float(vx) + float(w))**2 + float(vy)**2) # equation that determines velocity

sine001 = (float(vy) / float(v))    # sin(0) equation

cos01 = (float(vx) + float(w)) / float(v) # cos(0) equation

d1 = (float(v)*float(cos01)/float(g)) # distance formula w/cos
d2 = (float(v)*float(sine001) + math.sqrt((float(v)*float(sine001))**2 + 2*float(g)*float(y0))) # distance formula w/sin
d3 = float(d1) * float(d2)     # distance answer


tyards = float(d3) * 1.09361 # yards conversion from meters total
yards = math.floor(tyards) # round down yards
ryards = tyards - yards # remaining yards

tfeet = ryards * 3 # conversion to feet total
feet = math.floor(tfeet) # feet round down
rfeet = tfeet - feet # remaining feet

inches = rfeet * 12 # inches from feet conversion total
finalinches = math.floor(inches) # inches round down

if yards > 0:
    print("The horizontal distance travelled by the projectile is: ", yards, "yd", feet, "ft", finalinches, "in")
else:
    if yards < 0:
        print("The horizontal distance travelled by the projectile is: ", feet, "ft", finalinches, "in")
    else:

        if feet > 0:
            print("The horizontal distance travelled by the projectile is: ", feet, "ft", finalinches, "in")

        else:
            print("The horizontal distance travelled by the projectile is: ", finalinches, "in")
