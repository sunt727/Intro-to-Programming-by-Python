
#Compute approximate value for pi
pi = 355/113
radius = 2.2
area = pi*(radius**2)
circumference = pi*(radius*2)

print(circumference)

#
## change value of radius <- a stupid comment
## use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
#
## recalculate area using new values
area = pi*(radius**2)
print(area)
#
#
##############################
##### COMMENTING LINES #######
##############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
## do CTRL+1 again to uncomment them

#x = 10
#y = 20

x,y,z = 10,20,30
print("my fav num is", x, ".", "y =", y)

##Try Newton Raphson for cube root
#print('Find the cube root of x')
x = 9
g = 2.106575963718821
print('Current estimate cubed =', g**3)
nextGuess = g - ((g**3 - x)/(3*g**2))
print('Next guess to try =', nextGuess)


x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))
if x == y:
    print("x and y are equal.")
    y = int(input("Enter a different number for y: "))
if x < y:
    print("x is smaller")
    if x < y/10 and x > y/100:
        print('x is an order of magnitute smaller')
    elif x < y/100:
        print('x is more than an order of magnitute smaller')
else:
    print("x is not smaller")
print("thanks!")

##############################
##### AUTOCOMPLETE #######
##############################
## Spyder can autocomplete names for you
## start typing a variable name defined in your program and hit tab 
## before you finish typing -- try it below
#
## define a variable
#a_very_long_variable_name_dont_name_them_this_long_pls = 0
#
## below, start typing a_ve then hit tab... cool, right!
## use autocomplete to change the value of that variable to 1
#
## use autocomplete to write a line that prints the value of that long variable
## notice that Spyder also automatically adds the closed parentheses for you!
