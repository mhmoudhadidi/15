def on_forever():
    while input.is_gesture(Gesture.SHAKE):
        basic.show_string("Erathquake")      
    basic.show_icon(IconNames.SQUARE)  
basic.forever(on_forever)