# === villain (PixelPAD Export: Horror game) ===

# --- Start Logic ---
#villain start
self.sprite = sprite("villain.png" , 1, 7)

walking = new_animation(self.sprite, 10, 0, 6)
set_animation(self, walking)

self.scaleX = 0.5
self.scaleY = 0.5

self.x = 1158
self.y = 279

self.speed = 3
self.range = 400

# --- Loop Logic ---
#villain loop

dx = game.tom.x - self.x
dy = game.tom.y - self.y

if abs(dx) < self.range and abs(dy) < self.range: 
    
    if dx > 0:
        self.x += self.speed 
        self.scaleX = 0.5
    elif dx < 0: 
        self.x -= self.speed 
        self.scaleX = -0.5

    if dy > 0: 
        self.y += self.speed
    elif dy < 0: 
        self.y -= self.speed
