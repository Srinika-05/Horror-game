# === Camera (PixelPAD Export: Horror game) ===

# --- Start Logic ---
#Camera start
self.speed = 0.075

self.visible = False

# --- Loop Logic ---
#Camera loop
self.z = game.tom.z = 5000

xToMove = (game.tom.x - self.x) * self.speed
yToMove = (game.tom.y - self.y) * self.speed

self.x += xToMove
self.y += yToMove

if self.x > 650 + 900:
    self.x = 650 + 900
if self.x < -150: 
    self.x = -150
if self.y > 590:
  self.y = 590
if self.y < -400:
    self.y = -400

camera_set(self.x, self.y)
