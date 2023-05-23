basic.forever(function on_forever() {
    while (input.isGesture(Gesture.Shake)) {
        basic.showString("Erathquake")
    }
    basic.showIcon(IconNames.Square)
})
