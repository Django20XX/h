def Level_2_scorer():
    if game.score() >= 4:
        for index in range(4):
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
        Level_3()
    else:
        game.game_over()

def on_button_pressed_a():
    global Object2, Sprite
    Sprite.delete()
    Object2.delete()
    game.set_score(0)
    basic.show_string("Normal mode")
    Object2 = game.create_sprite(0, 0)
    Sprite = game.create_sprite(randint(1, 4), randint(1, 4))
input.on_button_pressed(Button.A, on_button_pressed_a)

def Level_3_scorer():
    if game.score() >= 5:
        for index2 in range(4):
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
        Level_4()
    else:
        game.game_over()

def on_gesture_logo_up():
    Sprite.change(LedSpriteProperty.Y, 1)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def Level_2():
    global Object2, Sprite
    Sprite.delete()
    Object2.delete()
    game.set_score(0)
    basic.show_string("Level 2")
    basic.show_string("3 2 1 Go!")
    Object2 = game.create_sprite(randint(0, 4), randint(0, 4))
    Sprite = game.create_sprite(randint(0, 4), randint(0, 4))
    basic.pause(15000)
    Level_2_scorer()

def on_gesture_tilt_left():
    Sprite.change(LedSpriteProperty.X, -1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def Level_1():
    global Object2, Sprite
    Sprite.delete()
    Object2.delete()
    game.set_score(0)
    basic.show_string("Level 1")
    basic.show_string("3 2 1 Go!")
    Object2 = game.create_sprite(randint(0, 4), randint(0, 4))
    Sprite = game.create_sprite(randint(0, 4), randint(0, 4))
    basic.pause(15000)
    Level_1_scorer()
def Level_1_scorer():
    if game.score() >= 3:
        for index3 in range(4):
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
        Level_2()
    else:
        game.game_over()
def Level_4():
    basic.show_leds("""
        . . . . #
                . . . # .
                . . . # .
                # . # . .
                . # . . .
    """)

def on_button_pressed_ab():
    game.show_score()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Speed mode")
    Level_1()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    Sprite.change(LedSpriteProperty.X, 1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def Scorer():
    game.add_score(1)
    Sprite.set(LedSpriteProperty.X, randint(0, 4))
    Sprite.set(LedSpriteProperty.Y, randint(0, 4))
    Object2.set(LedSpriteProperty.X, randint(0, 4))
    Object2.set(LedSpriteProperty.Y, randint(0, 4))

def on_gesture_logo_down():
    Sprite.change(LedSpriteProperty.Y, -1)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def Level_3():
    global Object2, Sprite
    Sprite.delete()
    Object2.delete()
    game.set_score(0)
    basic.show_string("Level 2")
    basic.show_string("3 2 1 Go!")
    Object2 = game.create_sprite(randint(0, 4), randint(0, 4))
    Sprite = game.create_sprite(randint(0, 4), randint(0, 4))
    basic.pause(15000)
    Level_3_scorer()
Object2: game.LedSprite = None
Sprite: game.LedSprite = None
game.set_score(0)
basic.show_string("Hi")
basic.show_string("Press A or B to start ")
Sprite = game.create_sprite(randint(1, 4), randint(1, 4))
Object2 = game.create_sprite(0, 0)

def on_forever():
    if Sprite.is_touching(Object2):
        Scorer()
basic.forever(on_forever)
