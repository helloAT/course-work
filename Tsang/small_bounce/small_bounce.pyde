y = 700
x = 383
done = False

def setup():
    background(0)
    size(1366, 700)

def draw():
    global x
    global y
    global done
    
    if x >= 983:
        done = True
    else:
        done = False
        
    if done:
        x -= 30
    else:
        x += 30
    
    y = (x - 983)*(x - 383)
    
    ellipse(x, y, 50, 50)
        
    
