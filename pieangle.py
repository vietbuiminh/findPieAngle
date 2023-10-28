from graphics import *
import graphics
from tkinter.filedialog import askopenfilename
from PIL import Image
import math
import button as bt
import numpy as np


def distanceBetween(point1, point2):
    '''
    Calculates the distance between two points

    Params:
    point1 (Point): the first point
    point2 (Point): the second point

    Returns:
    the distance between the two points
    '''
    diffX = point2.getX() - point1.getX()
    diffY = point2.getY() - point1.getY()
    return math.sqrt(diffX**2 + diffY**2)


def drawCircle(point, window):
    circle = Circle(point, 10)
    circle.setFill("red")
    circle.draw(window)


def drawLine(point1, point2, window):
    line = Line(point1, point2)
    line.setOutline("red")
    line.setWidth(2)
    line.draw(window)


def main():
    filename = askopenfilename()
    print(filename[filename.rfind("."):])
    if filename[filename.rfind("."):] != '.gif':
        print("File type does not work")
        print("Attempt to convert")
        img_o = Image.open(filename)
        img_o.save(filename[:filename.rfind("/")] +
                   filename[filename.rfind("/"):filename.rfind(".")+1]+"gif")
        filename = filename[:filename.rfind(
            "/")] + filename[filename.rfind("/"):filename.rfind(".")+1]+"gif"
        print(filename)

    img = Image.open(filename)
    w, h = img.size
    win = GraphWin("My Circle", w, h)

    display_img = graphics.Image(Point(w/2, h/2), filename)
    display_img.draw(win)
    point1 = win.getMouse()  # pause for click in window
    drawCircle(point1, win)
    point2 = win.getMouse()
    drawCircle(point2, win)
    drawLine(point1, point2, win)
    point3 = win.getMouse()
    drawCircle(point3, win)
    point4 = win.getMouse()
    drawCircle(point4, win)
    drawLine(point3, point4, win)
    a = distanceBetween(point1, point2)
    b = distanceBetween(point3, point4)
    print(f'a = {a}')
    print(f'b = {b}')
    ratio = 1.0
    if a >= b:
        ratio = b/a
    else:
        ratio = a/b
    if w > h:
        h = h*ratio
    else:
        w = w * ratio
    img = img.resize((int(w), int(h)))
    resize_name = filename[:filename.rfind(
        "/")] + filename[filename.rfind("/"):filename.rfind(".")]+"_resized"+".gif"
    img.save(resize_name)
    win.close()
    img = Image.open(resize_name)
    w, h = img.size
    win = GraphWin("Resize img", w, h)
    display_img = graphics.Image(Point(w/2, h/2), resize_name)
    display_img.draw(win)
    button = bt.Button(win, Point(w/2, h-30), 100, 30, ">")
    # frame_circle = Circle(Point(w/2, h/2), 20)
    point1 = win.getMouse()
    drawCircle(point1, win)
    point2 = win.getMouse()
    drawCircle(point2, win)
    drawLine(point1, point2, win)
    point3 = win.getMouse()
    drawCircle(point3, win)
    drawLine(point2, point3, win)
    p0 = [point1.getX(), point1.getY()]
    p1 = [point2.getX(), point2.getY()]
    p2 = [point3.getX(), point3.getY()]
    v0 = np.array(p0) - np.array(p1)
    v1 = np.array(p2) - np.array(p1)
    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
    angle_circle = Circle(point2, 30)
    angle_circle.draw(win)
    angle_text = bt.Button(win, Point(
        point2.getX()-20, point2.getY()-20), 40, 20, f"{round(abs(np.degrees(angle)), 2)}°")

    win.getMouse()
    win.close()


main()
