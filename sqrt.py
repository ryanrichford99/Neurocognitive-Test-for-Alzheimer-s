from math import sqrt
import cmath

icon1X = 20000
icon1Y = 20
playerX = 40
playerY = 600

if icon1X:
    distance = cmath.sqrt((playerX - playerY) ^ 2 + (icon1X - icon1Y) ^ 2)
    print("distance", distance)
else:
    print("no")

