import cv2
import turtle
import numpy as np
from matplotlib import pyplot as plt
import time

turtle.tracer(0)
turtle.bgcolor("white")  # Set the background color to white

def find_closest(p, positions):
    if len(positions) > 0:
        nodes = np.array(positions)
        distances = np.sum((nodes - p) ** 2, axis=1)
        i_min = np.argmin(distances)
        return positions[i_min]
    else:
        return None

def outline(image):
    src_image = cv2.imread(image, 0)
    blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
    th3 = cv2.adaptiveThreshold(blurred, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                thresholdType=cv2.THRESH_BINARY, blockSize=9, C=2)
    return th3

def draw_image(image, x, y):
    im = cv2.imread(image, 0)
    th3 = outline(image)

    WIDTH = im.shape[1]
    HEIGHT = im.shape[0]
    CUTOFF_LEN = ((WIDTH + HEIGHT) / 2) / 60  # Adjust the threshold value

    iH, iW = np.where(th3 == [0])
    iW = iW - WIDTH / 2 + x  # Add x offset
    iH = -1 * (iH - HEIGHT / 2 + y)  # Add y offset
    positions = [list(iwh) for iwh in zip(iW, iH)]
    print(positions)

    t = turtle.Turtle()
    t.color("brown")
    t.shapesize(1)
    t.pencolor("gray30")

    t.speed(0)
    t.penup()
    t.goto(positions[0])
    t.pendown()

    #time.sleep(1)

    p = positions[0]
    while p:
        p = find_closest(p, positions)
        if p:
            current_pos = np.asarray(t.pos())
            new_pos = np.asarray(p)
            length = np.linalg.norm(new_pos - current_pos)
            if length < CUTOFF_LEN:
                t.goto(p)
                turtle.update()
            else:
                t.penup()
                t.goto(p)
                t.pendown()
            positions.remove(p)
        else:
            p = None

    t.penup()
    t.hideturtle()
    time.sleep(1)

# List of image file paths
image_files = ['capacitor.png', 'resistor.png', 'battery.png','inductor.png']
image_positions = [(-400,100),(0, 0), (250, 0), (450, 0)]  # Set the positions for each image

for image_file, (x, y) in zip(image_files, image_positions):
    draw_image(image_file, x, y)

turtle.done()
