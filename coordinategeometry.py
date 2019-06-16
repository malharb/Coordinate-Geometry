import time
print("This program will help you find the distance between, midpoint of, and gradient of 2 points")
time.sleep(1)


def distance(x1,y1,x2,y2):
    dis_1 = x2 - x1
    dis_1i = dis_1**2

    dis_2 = y2 - y1
    dis_2i = dis_2**2

    distance_totalp= dis_1i + dis_2i
    distance_total = distance_totalp**0.5

    print("The distance between the points ({},{}) and ({},{}) is {} units".format(x1,y1,x2,y2,distance_total))

def midpoint(x1,y1,x2,y2):
    mp_xi = x1 + x2
    mp_x = mp_xi/2

    mp_yi = y1 + y2
    mp_y = mp_yi/2

    print("The midpoint of the two points ({},{}) and ({},{}) is ({},{})".format(x1,y1,x2,y2,mp_x,mp_y))

def gradient(x1,y1,x2,y2):
    gradient_y = y2 - y1
    gradient_x = x2 - x1
    gra = gradient_y / gradient_x

    print("The gradient of the line joining point ({},{}) and ({},{}) is {}".format(x1,y1,x2,y2,gra))


def configuration():
    x1 = input("Please enter the first x value: ")
    x1 = int(x1)
    y1 = input("Please enter the first y value: ")
    y1 = int(y1)

    x2 = input("Please enter the second x value: ")
    x2 = int(x2)
    y2 = input("Please enter the second y value: ")
    y2 = int(y2)

    distance(x1,y1,x2,y2)
    midpoint(x1,y1,x2,y2)
    gradient(x1,y1,x2,y2)

configuration()
input('Press ENTER to exit')
