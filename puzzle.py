#!/usr/bin/env python
# from random import randint
import sys

# Functions

# Main routine

print "Welcome to Puzzle!"
print
x = 0
while x < 4 :
  sys.stdout.write("a")
  if x < 1:
    sys.stdout.write(" ")
  sys.stdout.write("n")
  if x > 1:
    sys.stdout.write(" oyster\n")
    x = x + 2
  if x == 1:
    sys.stdout.write("noys\n")
  if x < 1:
    sys.stdout.write("oise\n")
  x = x + 1
