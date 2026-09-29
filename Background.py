# === Background (PixelPAD Export: Horror game) ===

# --- Start Logic ---
#Background start
self.sprite = sprite("forests.png")

self.scaleX = 0.4
self.scaleY = 0.4
self.z = -10

self.x = 700
self.y = 100

# --- Loop Logic ---
#Background loop
self.z = game.tom.z - 1000
self.z = game.larry.z - 1000
