# === coins (PixelPAD Export: Horror game) ===

# --- Start Logic ---
#coins start
import random
self.sprite = sprite("coins.png" , 1 , 10)

walking = new_animation(self.sprite, 10, 0, 9)
set_animation(self, walking)

self.scaleX = 0.25
self.scaleY = 0.25

self.x = random.randint(-150, 1550)
self.y = random.randint(-400, 590)

game.score = 0

# --- Loop Logic ---
#coins loop

if collision_check(self, "character"):
    game.score = game.score + 1
    destroy(self)
    print(game.score)
