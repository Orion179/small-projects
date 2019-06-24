import pyglet
from pyglet.window import key
#Opens a window with some floating text (Like the old Windows 7 sleep screen)
window = pyglet.window.Window()
label = pyglet.text.Label('Im just surprised this works', x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
#Adds movesment
def update(dt):
  print(dt)
  label.x += 1
  label.y += 1
#Prints some indications taht keys were pressed
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')
#Displays the message
@window.event
def on_draw():
  window.clear()
  label.draw()

pyglet.clock.schedule(update)
pyglet.app.run()