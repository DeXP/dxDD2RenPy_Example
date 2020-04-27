#
# dxDD2RenPy 0.8.0 by DeXPeriX
# The file was generated from Loops.json
# Generation date: 27.04.2020 19:59:08
# Please do not edit the file manually
# All changes will be lost after regeneration
# You can find more info about dxDD2RenPy on https://dexp.in/dxDD2RenPy
#
label Loops:
    show DeXP oho with dissolve
    DeXP "Do you want to hear about loops? Wow!"
    $ count9900232 = 0
    jump node9900232
    return

label node9900232:
    window hide
    while count9900232 < 2:
        $ count9900232 += 1
        DeXP "You will read this message 2 times. With random pose change each time"
        $ random3289257 = renpy.random.randint(1, 3)
        if random3289257 == 1:
            show DeXP norm with dissolve
            jump node1790898
        elif random3289257 == 2:
            show DeXP ha with dissolve
            jump node1790898
        elif random3289257 == 3:
            show DeXP oho with dissolve
            jump node1790898
    DeXP "That's basically it. You seen repeat loop and random branch "
    $ random7113403 = renpy.random.randint(1, 100)
    if random7113403 <= 33:
        show DeXP ha with dissolve
        DeXP "Also you lucky enough to see rare chance text!"
    else:
        DeXP "See you on other tutorials"
    return

label node1790898:
    window hide
    $ random1790898 = renpy.random.randint(1, 100)
    if random1790898 <= 70:
        jump node9435787
    else:
        DeXP "Rare message"
        jump node9435787
    return

label node9435787:
    window hide
    DeXP "Pose changed"
    jump node9900232
    return
