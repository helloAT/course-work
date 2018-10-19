import random
y = 50
x = 50
left = False
bottom = False

def setup():
    size(1366, 768)

def draw():
    global x
    global y
    global left
    global bottom
    background(100, 150, 255)
    fill(100, 255, 100)
    noStroke()
    rect(0, 650, 2000, 200)
    img = loadImage("i.png")
    
    if x >= 1300:
        left = True
    elif x <= 10:
        left = False
    if y >= 600:
        bottom = True
    elif y <= 10:
        bottom = False
    
    image(img, x, y, 200, 200)
    
    if left:
        x -= random.randint(30, 40)
    else:
        x += random.randint(30, 40)
    if bottom:
        y -= random.randint(30, 40)
    else:
        y += random.randint(30, 40)
