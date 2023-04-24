from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def move(self,pressed_keys,universal_speed):
      if pressed_keys[K_UP]:
          self.rect.move_ip(0,-1)
      if pressed_keys[K_DOWN]:
          self.rect.move_ip(0,1)
      if pressed_keys[K_RIGHT]:
          self.x = self.x + universal_speed
          self.rect.x = self.x
          # self.rect.move_ip(1,0)
      if pressed_keys[K_LEFT]:
          self.x = self.x - universal_speed
          self.rect.x = self.x
          # self.rect.move_ip(-1,0)
