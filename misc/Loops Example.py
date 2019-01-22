'''
    This code snippet demonstrates different types of 
    loops in Python for beginning students

    for loops iterate a number of times specified in 
    advance or through a variable. Iterate means one 
    pass through the loop
'''

for i in range(0, 10):
    print(i)  # write the value of i to the screen

''' 
    Breaking it down: i is a variable that counts the current 
    iteration number of the loop. range(0,10) is a standard function 
    that returns a list of numbers from 0 to 9. This loop will iterate
    10 times before it finishes.
    run it to see the value of i for each loop
'''

# you can also run a for loop backwards by passing a step 
# parameter of -1 to the range() function

for i in range(10, 0, -1):
    print(i)

# while loops run as long as the condition evaluates to True
# this loop will run forever because the condition is forced to be True. It can never become false.

i = 0
while True:
    print(i)
    i = i + 1  # add one to the current value of i and store it back to i

''' 
    Let's make a while loop that stops after 10 loops
    Our condition says to run as long as i is less than 10. 
    Make sure that your condition will become false at some point or else it will run forever.
'''

i = 0
while i < 10:
    print(i)
    i = i + 1  # add one to the current value of i and store it back to i
