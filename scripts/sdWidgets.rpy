
python early:
    def editoverlay():
        if sdStart:
            if persistent.sdWidgetPts:
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=2, xpadding=6, xminimum=200)
                ui.text("%s" % (save_name), style="button_text", size=13)           
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if ptsus <= 20:
                    ui.text("%s: %d" % ("Ульяна", ptsus), style="button_text", size=13)
                elif ptsus <= 8:
                    ui.text("%s: %d" % ("Ульяна", ptsus), style="button_text", size=14, color="#99ff33")
                else:
                    ui.text("%s: %d" % ("Ульяна", ptsus), style="button_text", size=15, color="#ff3200")
        
                ui.button(clicked=None, xpos=0.87, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if ptsmi <= 24:
                    ui.text("%s: %d" % ("Мику", ptsmi), style="button_text", size=13)
                elif ptsmi <= 8:
                    ui.text("%s: %d" % ("Мику", ptsmi), style="button_text", size=14, color="#99ff33")
                else:
                    ui.text("%s: %d" % ("Мику", ptsmi), style="button_text", size=15, color="#00bbbb")
                ui.button(clicked=None, xpos=0.75, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if ptsdv <= 30:
                    ui.text("%s: %d" % ("Алиса", ptsdv), style="button_text", size=13)
                elif ptsdv <= 12:
                    ui.text("%s: %d" % ("Алиса", ptsdv), style="button_text", size=14, color="#99ff33")
                else:
                    ui.text("%s: %d" % ("Алиса", ptsdv), style="button_text", size=15, color="#bb8800")
            
                ui.button(clicked=None, xpos=0.62, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if ptssl <= 25:
                    ui.text("%s: %d" % ("Славя", ptssl), style="button_text", size=13)
                elif ptssl <= 9:
                    ui.text("%s: %d" % ("Славя", ptssl), style="button_text", size=14, color="#99ff33")                
                else:
                    ui.text("%s: %d" % ("Славя", ptssl), style="button_text", size=15, color="#bbb200")
            
                ui.button(clicked=None, xpos=0.49, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if ptsun <= 30:
                    ui.text("%s: %d" % ("Лена", ptsun), style="button_text", size=13)
                elif ptsun <= 10:
                    ui.text("%s: %d" % ("Лена", ptsun), style="button_text", size=14, color="#99ff33")                  
                else:
                    ui.text("%s: %d" % ("Лена", ptsun), style="button_text", size=15, color="#9f72be")
                
                ui.button(clicked=None, xpos=0.4, xanchor=1.0, ypos=2, xpadding=6, xminimum=160)
                ui.text("%s: %d" % ("Настроение", mood), style="button_text", size=13)
                
                ui.button(clicked=None, xpos=0.3, xanchor=1.0, ypos=2, xpadding=6, xminimum=200)
                if impression >= 80:
                    ui.text("%s: %s" % ("Впечатление", "Оч. Хороший"), style="button_text", size=13, color="#00cc00")
                elif impression >= 60:
                    ui.text("%s: %s" % ("Впечатление", "Хороший"), style="button_text", size=13, color="#99ff33")
                elif impression >= 40:
                    ui.text("%s: %s" % ("Впечатление", "Нейтральный"), style="button_text", size=13, color="#ffff66")
                elif impression >= 20:
                    ui.text("%s: %s" % ("Впечатление", "Плохой"), style="button_text", size=13, color="#ff6600")
                else:
                    ui.text("%s: %s" % ("Впечатление", "Оч. Плохой"), style="button_text", size=13, color="#ff0000")
    
    config.overlay_functions.append(editoverlay)
    def editoverlay():
        if sdStart:
            if persistent.sdWidgetClubs:
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=480, xpadding=0, xminimum=120)
                ui.text("Кружки:", style="button_text", size=13)           
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=500, xpadding=0, xminimum=120)
                if music_worker == False:
                    ui.text("%s: %d" % ("Музыкант", music), style="button_text", size=13)
                else:
                    ui.text("%s: %d" % ("Музыкант", music), style="button_text", size=15, color="#ff3200")
        
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=520, xpadding=6, xminimum=120)
                if cyber_worker == False:
                    ui.text("%s: %d" % ("Кибернетик", cyber), style="button_text", size=13)
                else:
                    ui.text("%s: %d" % ("Кибернетик", cyber), style="button_text", size=15, color="#00bbbb")
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=540, xpadding=6, xminimum=120)
                if mtmerc_worker == False:
                    ui.text("%s: %d" % ("Помощник", mtmerc), style="button_text", size=13)
                else:
                    ui.text("%s: %d" % ("Помощник", mtmerc), style="button_text", size=15, color="#bb8800")
            
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=560, xpadding=6, xminimum=120)
                if dining_worker == False:
                    ui.text("%s: %d" % ("Столовая", dining), style="button_text", size=13)               
                else:
                    ui.text("%s: %d" % ("Столовая", dining), style="button_text", size=15, color="#bbb200")
            
                ui.button(clicked=None, xpos=0, xanchor=0.0, ypos=580, xpadding=6, xminimum=120)
                if medic_worker == False:
                    ui.text("%s: %d" % ("Медпункт", medic), style="button_text", size=13)                  
                else:
                    ui.text("%s: %d" % ("Медпункт", medic), style="button_text", size=15, color="#9f72be")
    config.overlay_functions.append(editoverlay)

    def editoverlay():
        if sdStart:
            if persistent.sdWidgetDebug:
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=480, xpadding=6, xminimum=120)
                ui.text("DEBUG INFO:", style="button_text", size=13)           
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=500, xpadding=6, xminimum=120)
                ui.text("%s: %d" % ("IMPRESSION", impression), style="button_text", size=15, color="#ff3200")
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=520, xpadding=6, xminimum=120)
                ui.text("%s: %d" % ("ISASSINGED", isAssigned), style="button_text", size=15, color="#ff3200")
    config.overlay_functions.append(editoverlay)

label sdWidgetMenu:
    $ set_mode_nvl()
    "На данный момент:"
    "   Виджет отношений: "
    if not persistent.sdWidgetPts:
        extend "Выключен"
    else:
        extend "Включён"
        
    "   Виджет клубов: "
    if not persistent.sdWidgetClubs:
        extend "Выключен"
    else:
        extend "Включён"
    
    "   Виджет дебага: "
    if not persistent.sdWidgetDebug:
        extend "Выключен"
    else:
        extend "Включён"

    menu:
        "Переключить виджет отношений":
            
            if not persistent.sdWidgetPts:
                $ persistent.sdWidgetPts = True
                "Виджет включён"
            else:
                $ persistent.sdWidgetPts = False
                "Виджет выключен"

        "Переключить виджет кружков":
            
            if not persistent.sdWidgetClubs:
                $ persistent.sdWidgetClubs = True
                "Виджет включён"
            else:
                $ persistent.sdWidgetClubs = False
                "Виджет выключен"
                
        "Переключить виджет дебага":
            
            if not persistent.sdWidgetDebug:
                $ persistent.sdWidgetDebug = True
                "Виджет включён"
            else:
                $ persistent.sdWidgetDebug = False
                "Виджет выключен"
                
        "Выйти в меню":
            window hide 
            show screen sdMenu
            with fade2
            play music five_years fadein 3
            $ renpy.pause(hard = True)
            
    jump sdWidgetMenu
