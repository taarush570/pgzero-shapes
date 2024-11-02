import pgzrun

WIDTH = 500
HEIGHT = 400
#width and height of your output window

#putting the things you want to show on the screen
def draw():
    #starting corner 
    corner1 = (0,0)
    #width and height of rectangle
    w = WIDTH
    h = HEIGHT - 100
    #corner2
    corner2 = (w,h)

    #making rectangle
    rect = Rect(corner1,corner2)
    screen.draw.rect(rect, (0,0,255))

    #second rectangle
    corner3 = (40,70)
    corner4 = (250,120)
    rect2 = Rect(corner3,corner4)
    screen.draw.filled_rect(rect2, (255,0,0))

    #third rectangle
    corner5 = (400,100)
    corner6 = (40,100)
    rect3 = Rect(corner5,corner6)
    screen.draw.filled_rect(rect3, (245,66,197))

    #drawing a circle - position- (x,y) ; radius ; rgb values

    pos = (100,100)
    screen.draw.filled_circle(pos , 50 , (2,245,67))

    #drawing a line
    start_point = (200,400)
    end_point = (400,300)

    screen.draw.line(start_point,end_point, (255,0,0))

pgzrun.go()

