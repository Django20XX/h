function Level_2_scorer () {
    if (game.score() >= 4) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
        Level_3()
    } else {
        game.gameOver()
    }
}
input.onButtonPressed(Button.A, function () {
    Sprite.delete()
    Object2.delete()
    game.setScore(0)
    basic.showString("Normal mode")
    Object2 = game.createSprite(0, 0)
    Sprite = game.createSprite(randint(1, 4), randint(1, 4))
})
function Level_3_scorer () {
    if (game.score() >= 5) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
        Level_4()
    } else {
        game.gameOver()
    }
}
input.onGesture(Gesture.LogoUp, function () {
    Sprite.change(LedSpriteProperty.Y, 1)
})
function Level_2 () {
    Sprite.delete()
    Object2.delete()
    game.setScore(0)
    basic.showString("Level 2")
    basic.showString("3 2 1 Go!")
    Object2 = game.createSprite(randint(0, 4), randint(0, 4))
    Sprite = game.createSprite(randint(0, 4), randint(0, 4))
    basic.pause(15000)
    Level_2_scorer()
}
input.onGesture(Gesture.TiltLeft, function () {
    Sprite.change(LedSpriteProperty.X, -1)
})
function Level_1 () {
    Sprite.delete()
    Object2.delete()
    game.setScore(0)
    basic.showString("Level 1")
    basic.showString("3 2 1 Go!")
    Object2 = game.createSprite(randint(0, 4), randint(0, 4))
    Sprite = game.createSprite(randint(0, 4), randint(0, 4))
    basic.pause(15000)
    Level_1_scorer()
}
function Level_1_scorer () {
    if (game.score() >= 3) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
        Level_2()
    } else {
        game.gameOver()
    }
}
function Level_4 () {
    basic.showLeds(`
        . . . . #
        . . . # .
        . . . # .
        # . # . .
        . # . . .
        `)
}
input.onButtonPressed(Button.AB, function () {
    game.showScore()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Speed mode")
    Level_1()
})
input.onGesture(Gesture.TiltRight, function () {
    Sprite.change(LedSpriteProperty.X, 1)
})
function Scorer () {
    game.addScore(1)
    Sprite.set(LedSpriteProperty.X, randint(0, 4))
    Sprite.set(LedSpriteProperty.Y, randint(0, 4))
    Object2.set(LedSpriteProperty.X, randint(0, 4))
    Object2.set(LedSpriteProperty.Y, randint(0, 4))
}
input.onGesture(Gesture.LogoDown, function () {
    Sprite.change(LedSpriteProperty.Y, -1)
})
function Level_3 () {
    Sprite.delete()
    Object2.delete()
    game.setScore(0)
    basic.showString("Level 2")
    basic.showString("3 2 1 Go!")
    Object2 = game.createSprite(randint(0, 4), randint(0, 4))
    Sprite = game.createSprite(randint(0, 4), randint(0, 4))
    basic.pause(15000)
    Level_3_scorer()
}
let Object2: game.LedSprite = null
let Sprite: game.LedSprite = null
game.setScore(0)
basic.showString("Hi")
basic.showString("Press A or B to start ")
Sprite = game.createSprite(randint(1, 4), randint(1, 4))
Object2 = game.createSprite(0, 0)
basic.forever(function () {
    if (Sprite.isTouching(Object2)) {
        Scorer()
    }
})
