def on_a_pressed():
    global dado
    dado = randint(1, 3)
    if dado == 1:
        game.splash("NUMERO 1")
        music.ba_ding.play()
    if dado == 2:
        music.ba_ding.play()
    if dado == 3:
        music.ba_ding.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

dado = 0
dado = 0
scene.set_background_color(4)