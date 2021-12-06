import pgzrun 
#Program begins, and necessary modules are imported

finish_line = Actor ("finish_400")
car = Actor ("tinycar")

#Actors are set into position

car.x = 400
car.y = 500

finish_line.x = 400
finish_line.y = 100

#Controls are set
 
def update():
    if keyboard.right:
        car.x = car.x + 2

    elif keyboard.left:
        car.x = car.x - 2

    elif keyboard.up:
        car.y = car.y - 2

    elif keyboard.down:
        car.y = car.y + 2
#Checks if the car collides (with rect) into finish line
    finish = car.colliderect(finish_line)
    if finish:
        quit()

#draws car and finish line
def draw():
    screen.clear()
    finish_line.draw()
    car.draw()
    
pgzrun.go()
    


