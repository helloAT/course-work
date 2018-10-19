import random
sunx = 50
cloudx = 100
cloudy = 100
sunleft = False
sunbottom = False

def setup():
    size(1366, 768)

def draw():
    global sunx
    global suny
    global sunleft
    global sunbottom
    background(100, 150, 255)
    fill(100, 255, 100)
    noStroke()
    rect(0, 650, 2000, 200)
    sun = loadImage("i.png")
    cloud = loadImage("cloud.png")
    
    if sunx >= 1300:
        sunleft = True
    elif sunx <= 10:
        sunleft = False
    if suny >= 600:
        sunbottom = True
    elif suny <= 10:
        sunbottom = False
    
    image(sun, sunx, suny, 200, 200)
    
    if left:
        sunx -= random.randint(30, 40)
    else:
        sunx += random.randint(30, 40)
    if bottom:
        suny -= random.randint(30, 40)
    else:
        suny += random.randint(30, 40)
        
    
        
        
    
