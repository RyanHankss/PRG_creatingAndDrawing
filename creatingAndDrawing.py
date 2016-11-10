from swampy.World import World


world = World()


class Point(object):

    """
    This class refers to a point on a computer screen with only
    two dimensions

    attributes: (x, y)

    """


class Rectangle(object):

    """
    This class utilizes the point to represent the corner
    from which the object is then created

    attributes: (width, height, corner)

    """


class Circle(object):

    """
    This class represents a circle, the point is
    at the center and the circle is created from there

    attributes: (center, radius)

    """


def draw_rectangle(window, box, color):

    low_l = box.corner
    up_r = Point()
    up_r.x = box.corner.x + box.width
    up_r.y = box.corner.y + box.height
    b_box = [[low_l.x, low_l.y], [up_r.x, up_r.y]]
    window.rectangle(b_box, outline='blue', width=4, fill=color)


def draw_point(canv, po, color):
    bbox = [[po.x, po.y], [po.x, po.y]]
    drawn_canvas = world.ca(canv.width, canv.height)
    drawn_canvas.rectangle(bbox, width=2, fill=color)


def create_circle(x, y, radius):
    c = Circle()
    c.center = Point()
    c.center.x = x
    c.center.y = y
    c.radius = radius
    return c


def draw_circle(win, cir, color):
    win.circle([cir.center.x, cir.center.y], cir.radius, outline=None, fill=color)

# create a drawing canvas

canvas = world.ca(width=700, height=500, background='white')

re = Rectangle()
re.width = 250
re.height = 300
re.corner = Point()
re.corner.x = 50
re.corner.y = -30

draw_rectangle(canvas, re, 'blue')

pt = Point()

pt.x = 0
pt.y = 0

draw_point(canvas, pt, 'black')


first = create_circle(-50, -90, 99)
second = create_circle(30, -50, 50)
third = create_circle(100, -23, 33.3)


draw_circle(canvas, first, 'yellow')
draw_circle(canvas, second, 'grey')
draw_circle(canvas, third, 'green')


world.mainloop()
