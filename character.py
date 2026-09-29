# === character (PixelPAD Export: Horror game) ===

# --- Start Logic ---
#character start
self.sprite = sprite("mcharacterRun.png" , 1 , 12)

walking = new_animation(self.sprite, 10, 0, 11)
set_animation(self, walking)

game.mcx = self.x
game.mcy = self.y

self.x = 903
self.y = 429

self.idle = True

self.state = 'walk'

self.animationSpeed = 10

self.lookingDirection = 'down'

self.heart = heart()
self.heart2 = heart()
self.heart3 = heart()

self.health = 3 
self.loosehealth = True 

self.time = 900

display = new_text("1", 1000, -150)
display.fontSize = 300
display.color = "white"
display.visible = False

display2 = new_text("2", 1000, -150)
display2.fontSize = 300
display2.color = "white"
display2.visible = False

# --- Loop Logic ---
#character loop
import math 

self.z = self.y
#movement of the character
if key_is_pressed("w"):
    self.y += 5 
if key_is_pressed('a'):
    self.x -= 5
    self.scaleX = -1
if key_is_pressed('d'):
    self.x += 5
    self.scaleX = +1
if key_is_pressed('s'):
    self.y -= 5


if self.x > 2050:
    self.x = 2050
if self.x < -700: 
    self.x = -700
if self.y > 900:
  self.y = 900
if self.y < -700:
    self.y = -700


self.heart.x = self.x - 20
self.heart.y = self.y + 60

self.heart2.x = self.x + 10
self.heart2.y = self.y + 60

self.heart3.x = self.x + 40 
self.heart3.y = self.y +60

if collision_check(self , "villain") and self.time <= 10:
    self.health -= 1 
    self.time = 900
    self.loosehealth = False 
       
if self.loosehealth == False: 
    self.loosehealth = True

if self.health ==3:
    pass
if self.health ==2: 
    self.heart.visible = False
if self.health ==1: 
    self.heart2.visible = False
if self.health ==0: 
    self.heart3.visible = False
    set_room("gameOver")

self.time -= 10

# if game.score ==0:
#     display.visible = True
   
# elif game.score == 1: 
#     display2.visible = True
#     display.visible = False
