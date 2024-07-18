import math
from colour import Color

def cursorAngle(ox, oy, mx, my):
    # get distance between the two objects
    deltax = mx - ox
    deltay = my - oy

    angle = math.degrees(math.atan2(deltax, deltay))
    return angle

def calculateDistance(ox, oy, mx, my):
    # get distance between the two objects
    deltax = mx - ox
    deltay = my - oy

    distance = math.sqrt((deltax * deltax) + (deltay * deltay))
    return distance

def calculateColor(range, steps, type):
    
    if type == "bar":
        color = [0, 0, 0]
        red = Color("red")
        colors = list(red.range_to(Color("green"), steps))
        range = round(range)
        tcolor = colors[round(range)-1].rgb

        color[0] = tcolor[0]* 255
        color[1] = tcolor[1]* 255
        color[2] = tcolor[2]* 255

        return color
    elif type == "beam":
        color = [0, 0, 0]
        yellow = Color("yellow")
        colors = list(yellow.range_to(Color("red"), steps))
        range = round(range)
        tcolor = colors[round(range)-1].rgb

        color = (tcolor[0]* 255, tcolor[1]* 255, tcolor[2]* 255)

        return color
    elif type == "decay":
        color = [0, 0, 0]
        red = Color("red")
        colors = list(red.range_to(Color("yellow"), steps))
        range = round(range)
        tcolor = colors[round(range)-1].rgb

        color[0] = tcolor[0]* 255
        color[1] = tcolor[1]* 255
        color[2] = tcolor[2]* 255
        return color


def chargeClick(clickStatus, charge, tickrate, chargeLength):
    if clickStatus:
        charge+= .01
        if charge >= chargeLength:
            print("charged")
            charge = chargeLength
            print(charge)
            return charge
        else:
            print(charge)
        return charge
    else:
        if charge > 0:
            charge-=(1/tickrate) * 3
        else:
            charge = 0
        print(charge)
        return charge

    




    

    

    



