#name
#Delta Fighter
from gamelib import*
#objects and initial settings
game = Game(800,600,"Delta Fighter")
bk = Image("field_5.png",game)
logo = Image("logo.png",game)
play = Image("play.png",game)
play.y = 500
story = Image("story.png",game)
story.y = 200
storyImage = Image("storyImage.png",game)#add an object 
storyImage.visible = False#set the image visible = False
howtoplay = Image("howtoplay.png",game)
howtoImage = Image("howtoImage.png",game)
howtoImage.visible = False
howtoplay.y = 400

asteroids = []#empty list
for index in range(100):#add the images to the list
    asteroids.append(Animation("asteroid.gif",41,game,2173/41,52))
for index in range(100):#set each item list
    x = randint(100,700)
    y = -randint(100,10000)
    asteroids[index].moveTo(x,y)
    s = randint(3,8)
    asteroids[index].setSpeed(s,180)
    
hero = Image("hero.gif",game)
hero.y = 500
hero.ammo = 0
items = 0#tally all asteroids and all ammo that have either collided or
#moved off the screen at the bottom

stars = []
for index in range(100):
    stars.append(Animation("plasmaball1.png",11,game,352/11,32))
for index in range(100):#set each item list
    
    x = randint(100,700)
    y = -randint(100,10000)
    stars[index].moveTo(x,y)
    s = randint(3,8)
    stars[index].setSpeed(s,180)

explosion = Animation("explosion1.png",22,game,1254/22,64)
explosion.resizeBy(70)
explosion.visible = False
game.setBackground(bk)

boss = Image("aliensh.png",game)
boss.resizeBy(-10)
boss.moveTo(boss.x,boss.y-200)
boss.setSpeed(1,180)

minions = []#alien attack

for index in range(100):
    minions.append(Image("alien2.png",game))
for index in range(100):#set each item list
    minions[index].resizeBy(-60)   
    x = randint(100,700)
    y = -randint(100,10000)
    minions[index].moveTo(x,y)
    s = randint(3,8)
    minions[index].setSpeed(s,180)
    
bullet = Animation("plasmaball2.png",10,game,640/10,64)
bullet.resizeBy(-50)
bullet.visible = False
explosion2 = Animation("plasmaball3.png",5,game,180/3,120/2)
explosion2.resizeBy(150)
explosion2.visible = False

#story.collisionBorder = "rectangle"
#Title Screen
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    logo.draw()
    story.draw()
    howtoplay.draw()
    play.draw()# add the play button
    storyImage.draw()#include the instruction to draw the storyImage
    howtoImage.draw()
    
    if storyImage.collidedWith(mouse) and mouse.LeftClick:
        storyImage.visible = False
    if story.collidedWith(mouse)and mouse.LeftClick:
        storyImage.visible = True
    if howtoImage.collidedWith(mouse) and mouse.LeftClick:
        howtoImage.visible = False
    if howtoplay.collidedWith(mouse)and mouse.LeftClick:
        howtoImage.visible = True
   
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over= True
   
    game.update(30)

game.over = False

#Level 1 Screen

while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    hero.draw()
    explosion.draw(False)#add false to stop the animation from looping
   
#move the asteroids; check for collision with hero and decrease hero health; see explosion; add to items accumulator
    for index in range(len(asteroids)):#the loop will go through the lis
        asteroids[index].move()
        if asteroids[index].collidedWith(hero):
            hero.health-=5#creates multiple hits?
            asteroids[index].visible = False
            explosion.moveTo(hero.x,hero.y - 30)#explosion should be on the hero ship
            explosion.visible = True
            items+=1#add to the total
      
        #check if each asteroid moves off screen and add to items accumulator   
        if asteroids[index].isOffScreen("bottom")and asteroids[index].visible:
            
            asteroids[index].visible = False
            items+=1
             
    for index in range(len(stars)):#the loop will go through the list
        stars[index].move()
        #check if hero catched a star and add to items accumulator
        if stars[index].collidedWith(hero):
            hero.ammo +=1
            stars[index].visible = False
            items+=1
        #check if each star is off the screen and add to items accumulator
        if stars[index].isOffScreen("bottom")and stars[index].visible:
            
            stars[index].visible = False
            items+=1
            
    if hero.health<0:
        game.over = True
        
    if items==len(asteroids) + len(stars):#is items value the exact match to the length of
        #the asteroids list and the stars lists
        game.over = True
        
    #if items >=200:
        #game.over = True
            
#Control the hero with the arrow keys 
    if keys.Pressed[K_LEFT]:
        hero.x-=3
    if keys.Pressed[K_RIGHT]:
        hero.x+=3
    if keys.Pressed[K_UP]:
        hero.y-=3
    if keys.Pressed[K_DOWN]:
        hero.y+=3
        
    if hero.health<=0:#one way to end the game - player will lose
        game.over = True
          
    game.drawText("Hero's Health: " + str(hero.health),hero.x,hero.y+20)
    game.drawText("Hero's Ammo: " + str(hero.ammo),hero.x,hero.y+40)
    game.drawText("Items: " + str(items),hero.x,hero.y+60)
    game.update(30)
game.over = False
hero.ammo = 50#temporarily to be able to play level 2


#Level 2 Screen - Boss and the alien invasion

while not game.over and hero.health>0:#modify to allow player to continue to game
    game.processInput()
    game.scrollBackground("down", 2)
    boss.move()
    hero.draw()
    bullet.draw()
    bullet.y-=100
    explosion2.draw(False)
      
    for index in range(len(minions)):#revise to for index in range(len(minions)):
        minions[index].move()

        if bullet.collidedWith(minions[index]):
            bullet.visible = False
            #other action?
        
    if keys.Pressed[K_SPACE]:#and not bullet.visible and hero.ammo>0:
        bullet.moveTo(hero.x,hero.y)
        bullet.visible = True
        hero.ammo-=1
    
    if bullet.collidedWith(boss):
        bullet.visible = False
        explosion2.moveTo(boss.x,boss.y)
        
        explosion2.visible = True
        boss.health-=10
        

    #if bullet.y<0:
        #bullet.visible = False

    #if bullet.isOffScreen("top")and not bullet.visible:
        #bullet.visible = True

    if hero.ammo<0 or hero.health<0:# a way to end the game and player lose
        game.over = True
        
    if keys.Pressed[K_LEFT]:
        hero.x-=3
    if keys.Pressed[K_RIGHT]:
        hero.x+=3

    if keys.Pressed[K_UP]:
        hero.y-=3
    if keys.Pressed[K_DOWN]:
        hero.y+=3    
              
    game.drawText("Hero's Health: " + str(hero.health),hero.x,hero.y+20)
    game.drawText("Hero's Ammo: " + str(hero.ammo),hero.x,hero.y+40)
    game.drawText("Boss Health: " + str(boss.health),boss.x,boss.y-150)
    game.update(30)
game.over = False
#End Screen
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    game.drawText("END SCREEN",300,300)
    
    
    
    game.update(30)
    
game.quit()


