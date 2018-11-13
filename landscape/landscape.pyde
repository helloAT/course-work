import random
sunx = 50
suny = 50
cloud1x = 0
cloud2x = 600
mariox = 300
marioleft = True
sunleft = False
sunbottom = False

def setup():
    global sunx, suny, cloud1x, cloud2x, mariox, marioleft, sunleft, sunbottom, sun, cloud, mario, tree
    size(1366, 768)
    sun = loadImage("angry_sun.png")
    cloud = loadImage("mario cloud.png")
    mario = loadImage("scared mario.png")
    tree = loadImage("tree.png")

def draw():
    draw_background()
    sun_movement()
    mario_movement()
    

def sun_movement():
    global sunx, suny, sunleft, sunbottom, sun
    if sunx >= 1200:
        sunleft = True
    elif sunx <= 10:
        sunleft = False
    if suny >= 600:
        sunbottom = True
    elif suny <= 10:
        sunbottom = False
    
    image(sun, sunx, suny, 150, 150)
    
    if sunleft:
        sunx -= 30
    else:
        sunx += 30
    if sunbottom:
        suny -= 30
    else:
        suny += 30
    
def mario_movement():
    global mariox, marioleft, mario
    if mariox <= 299:
        marioleft = True
    elif mariox >= 1066:
        marioleft = False
        
    if marioleft:
        mariox += 25
    else:
        mariox -= 25
        mario = loadImage("reverse mario.png")
        
    image(mario, mariox, 550, 145, 180)
    
def draw_background():
    global tree, cloud1x, cloud2x, cloud
    background(100, 150, 255)
    fill(100, 255, 100)
    noStroke()
    rect(0, 650, 2000, 200)
    image(tree, 150, 475, 250, 225)
    image(tree, 700, 475, 250, 225)
    cloud1x += 7
    cloud2x += 4
    if cloud1x >= 1366:
        cloud1x = 0
    if cloud2x >= 1366:
        cloud2x = 0
    image(cloud, cloud1x, 10, 100, 100)
    image(cloud, cloud2x, 100, 100, 100)
