#
# dxDD2RenPy 0.8.0 by DeXPeriX
# The file was generated from Main.json
# Generation date: 27.04.2020 19:59:08
# Please do not edit the file manually
# All changes will be lost after regeneration
# You can find more info about dxDD2RenPy on https://dexp.in/dxDD2RenPy
#
label Main:
    scene bg green
    show DeXP norm at center with moveinleft
    "Hi! My name is DeXPeriX"
    DeXP "I want to show you some basics"
    DeXP "The idea of this tutorial is that you will have alook on both execution and the source code."
    $ count9975669 = 0
    jump node9975669
    return

label node9975669:
    window hide

    menu:
        "What topic do you interested in?"

        "Choice menus":
            call Menu
            jump node9975669

        "Variables" if menuVisited:
            call Variables
            jump node9975669

        "Loops and chances":
            call Loops
            jump node9975669

        "Nothing":
            DeXP "I hope the tutorial was helpful to you"
            show DeXP ha with dissolve
            DeXP "Let's wait some time together"
            $ renpy.pause(2)
            "Good bye!"
    return
