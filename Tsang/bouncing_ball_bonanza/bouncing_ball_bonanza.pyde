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
    background(0)
    
    if x >= 1360:
        left = True
    elif x <= 10:
        left = False
    if y >= 695:
        bottom = True
    elif y <= 10:
        bottom = False
    
    noStroke()
    ellipse(x, y, 50, 50)
    if left:
        x -= random.randint(10, 20)
    else:
        x += random.randint(10, 20)
    if bottom:
        y -= random.randint(30, 40)
    else:
        y += random.randint(30, 40)
