init:

    $ randbg = "None"
    $ randtime = "None"
    
init python:

    def getrandback(bg, time):
        finalbg = "ext_" + bg + "_" + time
        renpy.scene()
        renpy.show(finalbg)
        
label sdWIPRoute:

    stop music fadeout 2
    stop ambience
    stop soundloop
    stop sound
    
    $ sdStart = False
    
    scene black with fade2
    
    play music always_summer fadein 4
    
    $ randbg = renpy.random.choice(["beach", "square", "path", "camp_entrance", "stage_normal", "playground", "island"])
    $ randtime = renpy.random.choice(["day", "night"])
    
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    
    $ getrandback(randbg, randtime)
    with Dissolve(3.0)
    show sdWIPRoute
    with Dissolve(1.5)
    $ renpy.pause(60)
    stop music fadeout 3

return

label sdComingSoonRoute:

    stop music fadeout 2
    stop ambience
    stop soundloop
    stop sound
    
    $ sdStart = False
    
    
    $ persistent.sprite_time = "prolog"
    $ prolog_time()

    scene black with fade2
    
    play music always_summer fadein 4
    
    $ randbg = renpy.random.choice(["beach", "square", "path", "camp_entrance", "stage_normal", "playground", "island"])
    $ randtime = renpy.random.choice(["day", "night"])
    
    $ getrandback(randbg, randtime)
    with Dissolve(3.0)
    show sdComingSoonRoute
    with Dissolve(1.5)
    $ renpy.pause(60)
    stop music fadeout 3
    
return

label sdComingSoonBranch:
    
    stop music fadeout 2
    stop ambience
    stop soundloop
    stop sound
    
    $ sdStart = False
    
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    
    scene black with fade2
    
    play music always_summer fadein 4
    
    $ randbg = renpy.random.choice(["beach", "square", "path", "camp_entrance", "stage_normal", "playground", "island"])
    $ randtime = renpy.random.choice(["day", "night"])
    
    $ getrandback(randbg, randtime)
    with Dissolve(3.0)  
    show sdComingSoonBranch
    with Dissolve(1.5)
    $ renpy.pause(60)
    stop music fadeout 3
    
return
    