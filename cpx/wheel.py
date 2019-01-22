import neopixel


# Input a value 0 to 255 to get a color value.
# The colours are a transition r - g - b - back to r.
def wheel(wheel_pos):
    wheel_pos = 255 - wheel_pos
    if wheel_pos < 85:
        return (255 - wheel_pos * 3, 0, wheel_pos * 3)
    elif wheel_pos < 170:
        wheel_pos -= 85
        return (0, wheel_pos * 3, 255 - wheel_pos * 3)
    else:
        wheel_pos -= 170
        return (wheel_pos * 3, 255 - wheel_pos * 3, 0)


# Returns the Red component of a color tuple
def get_red(color):
    return color[0]


# Returns the Green component of a color tuple
def get_green(color):
    return color[1]


# Returns the Blue component of a color tuple
def get_blue(color):
    return color[2]


# reduces the color brightness to 75%
def dim_color(color):
    dimmed_color = (get_red(color) >> 1, get_green(color) >> 1, get_blue(color) >> 1);
    return dimmed_olor;


test_value = 56

my_color = wheel(test_value)

print(my_color)
print(dim_color(my_color))
