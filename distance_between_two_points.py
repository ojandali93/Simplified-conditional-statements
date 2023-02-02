# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

def calculate_distance(a1, b1, a2, b2):
  distance = math.sqrt((a1-a2)**2 + (b1 - b2)**2)
  print('distance', distance)
  return distance

def calculate_length(a1, b1, a2, b2):
  length = math.sqrt((a1-a2)*(a1-a2) + (b1-b2)*(b1-b2))
  print('length', length)
  return length

xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35
# Calculate the distance between the two circle
distance = calculate_distance(xc1, yc1, xc2, yc2)
# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91
# calcualte the length of vector AB vector which is a vector between A and B points.
length = calculate_length(xa, ya, xb, yb)