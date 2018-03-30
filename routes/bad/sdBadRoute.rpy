label sdDinnerPrepare:

    jump sdWIPRoute
    
label sdConcertBadRouteSong:
    scene ext_stage_big_night with dissolve
    ""
    window hide
    play music sick_of_everyone fadein 5
    
    $ renpy.pause(26.0, hard = True)
    
    show sdTextBack with easeinbottom
    show sdSong sick_of_everyone_text1:
        xalign 0.5 
        ypos 1.0
        linear 80.0 ypos -1.0 
    
    $ renpy.pause(80.0, hard = True)
    
    hide sdSong with dissolve
    hide sdTextBack with easeoutbottom
    
    $ renpy.pause(7.0, hard = True)
    
    show sdTextBack with easeinbottom
    show sdSong sick_of_everyone_text2:
        xalign 0.5 
        ypos 1.0
        linear 55.0 ypos -1.0 
        
    $ renpy.pause(55.0, hard = True)
    
    hide sdSong with dissolve
    hide sdTextBack with easeoutbottom
    
    stop music fadeout 3
    ""
return
