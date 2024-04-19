# Import pyglet to create graphical window displays
import pyglet
from pyglet import shapes


def create_graphical_birthday_card(name):
    # Create a window
    window = pyglet.window.Window(width=800, height=600, caption='Happy Birthday!')

    # Preload resources
    label = pyglet.text.Label(f'Happy Birthday, {name}!',
                              font_name='Times New Roman',
                              font_size=24,
                              x=window.width//2, y=window.height//2,
                              anchor_x='center', anchor_y='center')

    # Define colors for cake layers
    cake_colors = [(255, 223, 186), (255, 180, 112), (255, 140, 26)]
    
    # Create multiple layers for the cake
    cake_layers = [
        shapes.Rectangle(window.width//2 - 120 + 10*i, window.height//2 - 150 + 30*i, 240 - 20*i, 30, color=cake_colors[i % 3], batch=None)
        for i in range(3)
    ]

    # Add candles on top
    candles = [
        shapes.Rectangle(window.width//2 - 60 + 30*i, window.height//2 - 90, 10, 40, color=(255, 69, 0), batch=None)
        for i in range(4)
    ]

    @window.event
    def on_draw():
        window.clear()
        for layer in cake_layers:
            layer.draw()
        for candle in candles:
            candle.draw()
        label.draw()


    # Run the application
    pyglet.app.run()


create_graphical_birthday_card("Adi")
