import pyglet
from pyglet.gl import *

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

window = pyglet.window.Window()

img= pyglet.image.load('assets/hero/Old hero.png')
smol_img = img.get_region(x=15,y=-40,width=24,height=25)
spr = pyglet.sprite.Sprite(smol_img, x=200, y=200)

img2= pyglet.image.load('assets/mario.0.jpg')
spr1 = pyglet.sprite.Sprite(img2, x = 10, y = 100)
spr1.scale = 0.18

img3= pyglet.image.load('assets/il_570xN.1259915155_jheb.jpg')
spr2= pyglet.sprite.Sprite(img3, x = 75, y = 100)
spr2.scale = 0.1



label = pyglet.text.Label('Welcome To My Game')
# font_name='Black Ops',
# font_size=40,
# x=window.width//2, y=window.height//2,
# anchor_x='center', anchor_y='center'

keys = pyglet.window.key.KeyStateHandler()




def update(dt):
  window.push_handlers(keys)
  if keys[pyglet.window.key.RIGHT]:
    spr.x += 1
  if keys[pyglet.window.key.LEFT]:
    spr.x -= 1
  if keys[pyglet.window.key.UP]:
    spr.y += 1
  if keys[pyglet.window.key.DOWN]:
    spr.y -= 1

  











@window.event
def on_draw():
    window.clear()
    label.draw()
    img.blit(150,100)
    spr.draw()
    spr2.draw()

# Start the event loop
pyglet.clock.schedule(update)
pyglet.app.run()



