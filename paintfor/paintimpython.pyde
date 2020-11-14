def setup():
    background(255)
    size(600,400)
    
def draw():
    if mouseButton == LEFT:
        background(255)
    if mouseButton == RIGHT:
        stroke(255,34,5)
        fill(255,34,5)
        ellipse(mouseX,mouseY,50,50)
    


    
