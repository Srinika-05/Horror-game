# === door (PixelPAD Export: Horror game) ===

# --- Start Logic ---
#door start
self.sprite = sprite("door.png")
self.x = -100
self.y = 860
self.z = 0

self.scaleX = 2
self.scaleY = 2

# --- Loop Logic ---
#door loop

if game.score == 5:  
    if collision_check(self, "character"):
        set_room("winGame")
