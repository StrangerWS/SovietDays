# ================================================================================== #
#                ОФИЦИАЛЬНАЯ ДОКУМЕНТАЦИЯ ФАЙЛА ИНИЦИАЛИЗАЦИИ                        #
# ================================================================================== #
# Файл сценария мода «Советские будни».                                              #
# Разработчик — StrangerWS, 2015-2016.                                               #
# ================================================================================== #

# =========== #
# Переменные  #
# =========== #

label initMap:
    $ sdInitMapZones()
    return

label initVars: 
    # Версия мода на данный момент.
    $ sd_version =      "pre0.3.5"
    
    # Переменные для отрисовки виджета.
    $ sdStart =                         False
    if not persistent.sdWidgetPts:
        $ persistent.sdWidgetPts =      False
    if not persistent.sdWidgetClubs:
        $ persistent.sdWidgetClubs =    False
    if not persistent.sdWidgetDebug:
        $ persistent.sdWidgetDebug =    False
    
    #======================================
    # persistent- переменные. На время тестирования - включены.
    $ persistent.sdAllEndings =     True
    $ persistent.sdDvEnding =       True
    $ persistent.sdUnEnding =       True
    $ persistent.sdUsEnding =       True
    $ persistent.sdSlEnding =       True
    $ persistent.sdMiEnding =       True
    $ persistent.sdUvEnding =       True
    $ persistent.sdAloneEnding =    True
    
    # persistent-переменные для ачивок. На время тестирования - отключены.
    
    $ persistent.sdAch_bridges =            False
    $ persistent.sdAch_cyber =              False
    $ persistent.sdAch_medic =              False
    $ persistent.sdAch_uvroute =            False
    $ persistent.sdAch_music =              False
    $ persistent.sdAch_dining =             False
    $ persistent.sdAch_mtmerc =             False    
    $ persistent.sdAch_firstChapterGirl =   False          
    $ persistent.sdAch_firstChapterAlone =  False
    $ persistent.sdAch_firstChapterTrue =   False   

    #======================================
    # Переменные первого дня
    
    # Если заметил девушку.
    $ slspotted =           False
    $ unspotted =           False
    
    # Доступ к карте.
    $ sdMap_1day =          0
    
    # Согласился присмотреть за Леной.
    $ unneedaid =           False
    
    # Если знаком с девушкой.
    $ slmet =               False
    $ unmet =               False 
    $ dvmet =               False
    $ usmet =               False
    
    # Если отшил вожатую с помощью.
    $ mt_denied_1day =      False
    
    # Номер дня - остров с Леной.
    $ un_island_day_number = 0
    
    # Знает, что Лена в медпункте
    $ knew_about_un_1day = False
    
    # Ужин для Лены.
    $ dinner_for_un_1day = False
    
    # Переменная задумки Алисы: 0 - не знал, -1 - не согласился, 1 - согласился.
    $ dv_deed_1day = 0
    
    # Футбол с СССР-тян
    $ us_football_1day =    False
    
    # =====================================
    # Переменные второго дня
    
    # Согласился посмотреть ТВ с Ульяной
    $ us_watch_tv_2day =    False
    
    # =====================================
   
    # Очки отношений - "сердце" мода
    $ ptsun =           0
    $ ptsdv =           0
    $ ptsus =           0
    $ ptssl =           0
    $ ptsmi =           0
    
    # + множитель от кружков (ОТКЛЮЧИТЬ)
    $ mulsl =           1.0
    $ mulmi =           1.0
    $ muldv =           1.0
    $ mulun =           1.0
    $ mulus =           1.0
    
    # Инициализируем кружки. Для вступления надо набрать не менее двух очков.
    $ music =           0
    $ cyber =           0
    $ mtmerc =          0
    $ medic =           0
    $ dining =          0
    $ isAssigned =      False
    
    $ music_worker =    False
    $ cyber_worker =    False
    $ mtmerc_worker =   False
    $ medic_worker =    False
    $ dining_worker =   False
    
    # Инициализируем настроение и впечатление. Если впечатление низкое - повышается шанс плохих событий, если высокое - сюжетная линия идёт своим ходом.
    # Настроение убирает возможность участвовать в каких-то событиях или выполнять поручения. 
    # С плохим настроением Александру больше хочется сидеть дома и никуда не выходить, либо общаться с друзьями.
    $ impression =      50
    $ mood =            100
    
    # Инициализируем переменные к ЮВАО-руту. Выход на него (должен быть) сложен, если не сверяться с таблицей/не обращать внимания на детали игры.
    $ uvroute =         0
    $ uvao_1day =       False
    
    # Для финала. Кидает на тот или иной кусок в зависимости от успеха прохождения.
    $ sdFirstChapter = "None"
    return

# =================== #
# Картинки и эффекты  #
# =================== #
    
label initImg:

    # Фоны
    image bg int_sasha_house_day =              sdGetImage("bg/int_extra_house_day.jpg")
    image bg int_sasha_house_night =            sdGetImage("bg/int_extra_house_night.jpg")
    image bg ext_city_day =                     sdGetImage("bg/ext_city_day.jpg")
    image bg int_classroom_day =                sdGetImage("bg/int_classroom_day.jpg")
    image bg ext_bus1 =                         sdGetImage("bg/ext_bus1.jpg")
    image bg ext_musclub_night =                sdGetImage("bg/ext_musclub_night.jpg")
    image bg ext_musclub_sunset =               sdGetImage("bg/ext_music_club_sunset.jpg")
    image bg int_musclub_day =                  sdGetImage("bg/int_music_club_day.jpg")
    image bg int_musclub_day_blur =             sdGetImage("bg/int_music_club_day_blur.png")
    image bg int_musclub_sunset =               sdGetImage("bg/int_music_club_sunset.jpg")
    image bg int_musclub_night =                sdGetImage("bg/int_music_club_night.jpg")
    image bg ext_musclub_verandah_day =         sdGetImage("bg/ext_music_club_verandah_day.jpg")
    image bg ext_musclub_verandah_night =       sdGetImage("bg/ext_music_club_verandah_night.jpg")
    image bg ext_sky =                          sdGetImage("bg/ext_sky.jpg")
    image bg ext_aidpost_sunset =               sdGetImage("bg/ext_aidpost_sunset.jpg")
    image bg ext_library_sunset =               sdGetImage("bg/ext_library_sunset.jpg")
    image bg int_dining_hall_people_sunset =    sdGetImage("bg/int_dining_hall_people_sunset.jpg")
    image bg int_sporthall =                    sdGetImage("bg/int_sport.jpg")
    image bg ext_old_building_day =             sdGetImage("bg/ext_old_building_day.jpg")
    image bg ext_old_building_sunset =          sdGetImage("bg/ext_old_building_sunset.jpg")
    image bg ext_old_building_rainy =           sdGetImage("bg/ext_old_building_rainy.jpg")
    image bg int_kitchen_day =                  sdGetImage("bg/int_kitchen_day.jpg")
    image bg int_kitchen_day2 =                 sdGetImage("bg/int_kitchen_day2.jpg")
    image bg ext_shower_day =                   sdGetImage("bg/ext_shower_day.jpg")
    image bg ext_houses_night =                 sdGetImage("bg/ext_houses_night.jpg")
    image bg ext_warehouse_day =                sdGetImage("bg/ext_warehouse_day.jpg")
    image bg ext_warehouse_night =              sdGetImage("bg/ext_warehouse_night.jpg")
    image bg int_warehouse_day =                sdGetImage("bg/int_shed.jpg")
    
    # CG разных сортов 
    image cg d1_dining_work_1 =                 sdGetImage("cg/d1_dining_work_1.jpg")
    image cg d1_dining_work_2 =                 sdGetImage("cg/d1_dining_work_2.jpg")
    
    # Анимации
    image anim sdDream:
        contains:
            "images/anim/prolog_1.jpg" with Dissolve(0.5, alpha=False)
            pause 0.5
            "images/anim/prolog_2.jpg" with Dissolve(0.5, alpha=False)
            pause 0.5
            repeat
            
    # Эффект - Надпись
    image effect_thatgirl =                     sdGetImage("gui/effect/thatgirl.png")
    
    # Эффект - Выбор цвета для мини-игры
    image effect_colorOverlayMeow:
        sdColorPick
        alpha 0.0
        linear 0.25 alpha 0.75
    
    # Отдельно для красного (получение урона)
    image effect_colorOverlayRed:
        "red"
        alpha 0.0
        linear 0.25 alpha 0.75
    
    # И цвета для эффекта
    image white =                               Solid("#FFFFFF")
    image green =                               Solid("#00FF00")
    image red =                                 Solid("#FF0000")
    image pink =                                Solid("#FF6699")
    image yellow =                              Solid("#FFFF00")
    image orange =                              Solid("#FF9900")
    image blue =                                Solid("#0000CD")
    image purple =                              Solid("#9900CC")
    image black =                               Solid("#000000")

    # Переходик
    $ sdTransition =                            ImageDissolve(sdGetImage("gui/effect/sdTransition.png"), 2.0, 50, reverse = False)
    
    # Дисклеймеры, баннеры, заглушки
    image sdDisclaimer =                        sdGetImage("gui/menu/sdDisclaimer.jpg")
    image sdWIPRoute =                          sdGetImage("gui/menu/sdWIPRoute.png")
    image sdComingSoonRoute =                   sdGetImage("gui/menu/sdComingSoonRoute.png")
    image sdComingSoonBranch =                  sdGetImage("gui/menu/sdComingSoonBranch.png")
    
    # Задник для текста
    image sdTextBack =                          sdGetImage("gui/menu/sdTextBack.png")
    
    # Ачивки!
    image sdAch_bridges =                       sdGetAchImage("bridges.png")
    image sdAch_cyber =                         sdGetAchImage("cyber.png")
    image sdAch_medic =                         sdGetAchImage("medic.png")
    image sdAch_uvroute =                       sdGetAchImage("uvao_route_start.png")
    image sdAch_music =                         sdGetAchImage("music.png")
    image sdAch_dining =                        sdGetAchImage("dining.png")
    image sdAch_mtmerc =                        sdGetAchImage("mtmerc.png")
    image sdAch_firstChapterGirl =              sdGetAchImage("to_be_continued.png")
    image sdAch_firstChapterAlone =             sdGetAchImage("maybe_continued.png")
    image sdAch_firstChapterTrue =              sdGetAchImage("uvao_confirmed.png")
    
    return

# ============== #
# Звуки и музыка #
# ============== #  
    
label initSnd:

    # Регистрируем дополнительные каналы на всякий случай
    $ renpy.music.register_channel("addsound", "sfx", False)
    $ renpy.music.register_channel("soundloop", "voice", True)
    $ renpy.music.register_channel("addsoundloop", "voice", True)
    
    # ========================================================================================
    # Музыка и эффекты с freesound.org
    $ dandelion =               sdGetMusic("dandelion.mp3")
    $ a_second_behind =         sdGetMusic("a_second_behind.mp3")
    
    # ========================================================================================
    # Кредиты: Группа - название, альбом, год
    # ========================================================================================
    # Saint Asonia - Trying To Catch Up With The World, Saint Asonia, 2015
    $ trying_to_catch_up =      sdGetMusic("trying_to_catch_up_with_the_world.mp3")
    
    # Saint Asonia - Fairy Tale (Acoustic), Saint Asonia, 2015
    $ fairytale_acoustic =              sdGetMusic("fairytale_acoustic.mp3")
    
    # Sum 41 - So Long Goodbye, Underclass Hero, 2007
    $ so_long_goodbye =                 sdGetMusic("so_long_goodbye.mp3")
    
    # Sum 41 - Sick Of Everyone, Screaming Bloody Murder, 2011
    $ sick_of_everyone =                sdGetMusic("sick_of_everyone.mp3")

    # Saltatio Mortis - Der Sandmann, Das schwarze Einmaleins, 2013
    $ der_sandmann =                    sdGetMusic("sandmann.mp3")
    
    # Versengold - Der Sandmann, 15 Jare - 15 Bands (Cover-сборник Saltatio Mortis), 2015
    $ der_sandmann_cover =              sdGetMusic("der_sandmann.mp3")
    
    # Yellowcard - Always Summer, Southern Air, 2012 - SOUNDTRACK
    $ always_summer =                   sdGetMusic("always_summer.mp3")
    
    # Drex Wiln - Flash Strike (Demo), Portfolio, 2015
    $ flash_strike =                    sdGetMusic("flash_strike_demo.mp3")
    
    # Drex Wiln - Scary Tale, Portfolio, 2015
    $ scarytale =                       sdGetMusic("scary_tale.mp3")
    
    # Smith & Myers – Wanted Dead or Alive (Bon Jovi cover), Acoustic Session, 2014
    $ wanted_dead_or_alive_cover =      sdGetMusic("wanted_dead_or_alive_sm.mp3")
    
    # Марлины - Пятилетка, К истокам, 2013 - ИНТРО
    $ five_years =                      sdGetMusic("five_years.mp3")
    
    # Марлины - Кто она, EP In Rock, 2016
    $ who_is_she =                      sdGetMusic("who_is_she.mp3")
    
    # =======================================================================================    
    # Звуки
    # =======================================================================================
    # Новый обеденный горн
    $ sdNewDinner =             sdGetSnd("sdNewDinner.mp3")
    
    # Горн перехода
    $ sdTransitionHorn =        sdGetSnd("sdTransitionHorn.mp3")
    
    # Звук подтверждения
    $ sdConfirm =               sdGetSnd("sdConfirm.mp3")
    
    # Боль
    $ sdGrunt =                 sdGetSnd("grunt.wav")
    
    # Клацанье зубами
    $ sdChatteringTeeth =       sdGetSnd("sdChatteringTeeth.mp3")
    
    # Выключатель
    $ sdSwitchEarNoise =        sdGetSnd("sdSwitchEarNoise.mp3")
    
    # Банки падают
    $ sdFallingCans =           sdGetSnd("sdFallingCans.mp3")
    
    # Звон цепи на двери
    $ sdChain =                 sdGetSnd("sdChain.mp3")

    # =======================================================================================
    
label initChars:

    # Новые персонажи
    $ sdme =    Character(u"Саша", color="FFFFFF", what_color="E2C778",) #E0000E - исходный
    $ nap =     Character(u"Повариха", color="00A000", what_color="E2C778",)
    $ na =      Character(u"Тётя Надя", color="00A000", what_color="E2C778",)
    
    # Хор, толпы и т.д.
    $ elme =    Character(u"{color=#FFFFFF}Саша{/color} {color=#80A055}|{/color} {color=#FFF226}Электроник{/color}", what_color = "#E2C778",)
    $ midv =    Character(u"{color=#00DEFF}Мику{/color} {color=#80A055}|{/color} {color=#FFAA00}Алиса{/color}", what_color="E2C778",)
    $ kids =    Character(u"Дети", color="FF6600", what_color="E2C778",)
    $ spk =     Character(u"Громкоговоритель", color="00A000", what_color="E2C778",)
    
    # Персонажи из снов
    $ drgl =    Character(u"Глашатай", kind = nvl, color="AB00A5", what_color="E2C778",)

    # Голоса, незнакомцы
    $ unk =     Character(u"Голос", color="E2C778", what_color="E2C778")  
    
# ===================================================== #
#  Функции, анимации и прямое взаимодействие с питоном  #
# ===================================================== #

init -5 python:

    def sdTimeskip():
        renpy.play(sdTransitionHorn)
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(sdTransition)
        renpy.music.stop(channel="sound", fadeout=2)

    def sdGetAch(img):
        renpy.play(sfx_achievement)
        renpy.show(img, [sdAchAnim])
        renpy.pause(4.5)
        renpy.hide(img) 
        
    def sd_chapter(sd_numday, sd_day):
        global save_name
        save_name = (u"СБ v.%s:День %d. %s") % (sd_version, sd_numday, sd_day)
    
    # Методы для реплик известного/неизвестного персонажа
    def usname(str):
        if usmet == True:
            return us(str)
        else:
            return usp(str)
        
    def dvname(str):
        if dvmet == True:
            return dv(str)
        else:
            return dvp(str)
            
init python:
    # Методы для ограничения значений впечатления и настроения        
    # Новый метод для универсальности
    def sdChangeImpression(var):
        global impression
        if var < 0:
            if impression + var < 0:
                impression = 0
            else:
                impression += var
        else:
            if impression + var > 100:
                impression = 100
            else:
                impression += var
    
    def sdChangeMood(var):
        global mood
        if var < 0:
            if mood + var < 0:
                mood = 0
            else:
                mood += var
        else:
            if mood + var > 100:
                mood = 100
            else:
                mood += var
    
    # Метод для проверки настроения
    def sdCheckMood():
        global mood
        if mood >= 80:
            return 2
        elif 60 <= mood < 80:
            return 1
        elif 40 <= mood < 60:
            return 0
        elif 20 <= mood < 40:
            return -1
        else:
            return -2
    
    # Методы для проверки на дружбу и любовь
    def sdCheckFriend(girl):
        if girl == "sl" and ptssl >= 7:
            return True
        elif girl == "un" and ptsun >= 10:
            return True
        elif girl == "dv" and ptsdv >= 12:
            return True
        elif girl == "mi" and ptsmi >= 8:
            return True
        elif girl == "us" and ptsus >= 8:
            return True
        else:
            return False
    
    def sdCheckLove(girl):
        if girl == "sl" and ptssl >= 25:
            return True
        elif girl == "un" and ptsun >= 30:
            return True
        elif girl == "dv" and ptsdv >= 30:
            return True
        elif girl == "mi" and ptsmi >= 24:
            return True
        elif girl == "us" and ptsus >= 20:
            return True
        else:
            return False
return

init -1000 python:
    sdDefautPath = "../559354092/SovietDays/"

init -998 python:
    def sdGetImage(file):
        return sdDefautPath + "res/image/%s" % (file)
    def sdGetAchImage(file):
        return sdDefautPath + "res/image/gui/ach/%s" % (file)
    def sdGetSnd(file):
        return sdDefautPath + "res/sound/%s" % (file)
    def sdGetMusic(file):
        return sdDefautPath + "res/music/%s" % (file)
        
python early:
    def sdPlayMod():
        sdDisc()
        if "customMainMusic" not in filters:
            config.main_menu_music = always_summer
        rgsn = renpy.game.script.namemap
        rgsn["prologue"],rgsn["sdPrologueOriginal"] = rgsn["sdPrologueOriginal"],rgsn["prologue"]
    
init -1 python:
    def sdDisc():
        config.label_overrides["splashscreen_2"] = "sdSplash"


# Менюшка ^_^       
screen sdMenu:

    tag menu
        
    imagemap: 
    
        ground  "SovietDays/res/image/gui/menu/sdMenu-static.jpg"
        hover   "SovietDays/res/image/gui/menu/sdMenu-hover.jpg"
        alpha True 
        
        hotspot (90, 932, 977, 1061)    action[OpenURL("vk.com/es_sdGroup")]
        hotspot (1057, 273, 1907, 398)  action[Jump("sdPrepare")]
        hotspot (1057, 398, 1907, 525)  action[Jump("sdTests")]
        hotspot (1057, 525, 1907, 660)  action[Return()] 
        hotspot (1057, 775, 1907, 885)  action MainMenu(confirm = False)
        

# Приближение/удаление и прочие воздействия на спрайты (на основе булок)
# Удаление не тестили, работаем без него
    
transform sdComeOnNormal:
    
    truecenter
    linear 5.0 zoom 1.5 ypos 0.25
    
transform sdComeOnFar:

    truecenter
    linear 5.0 zoom 1.5 ypos 0.40
    
transform sdGetUp:

    parallel:
        ease 1.0 ypos 0.0
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0
    
transform sdSitDown:
    
    parallel:
        ease 1.0 ypos 0.25
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0
        
transform sdSitCenter:
    xalign 0.5
    yanchor 0.0
    ypos 0.25

transform sdSitLeft:

    xalign 0.28
    xanchor 0.5
    yanchor 0.0
    ypos 0.25

transform sdSitRight:

    xalign 0.72
    xanchor 0.5
    yanchor 0.0
    ypos 0.25

transform sdSitLeftS:

    xalign 0.28
    xanchor 0.5
    yanchor 0.0
    ypos 0.15

transform sdSitCenterS:

    xalign 0.5
    yanchor 0.0
    ypos 0.15

transform sdSitRightS:

    xalign 0.72
    xanchor 0.5
    yanchor 0.0
    ypos 0.15 
 
transform sdAchAnim:
    pos(0.85, 0.85)
    anchor(0.5, 0.5)
    zoom 0.0
    ease 1.5 zoom 1.05 
    ease 0.25 zoom 0.95
    ease 0.25 zoom 1.0
    pause 1.0
    ease 0.5 pos(0.8, 0.85)
    ease 0.5 pos(1.0, 0.85) alpha 0.0
 
# Дальше - самописные эффекты
 
transform sdJumping:
    
    yanchor 0.0
    linear 0.3 ypos 0.1
    linear 0.3 ypos 0.0
    repeat
    
transform sdCarrying:

    anchor (0.5, 0.5) pos (0.15, 0.7) zoom 1.2
    
transform sdCarryingS:

    anchor (0.5, 0.5) pos (0.15, 0.5) zoom 1.2

transform sdRunningchar:

    anchor (0, 0) pos (2,0)    
    linear 2.0 xpos -1.0
    pause 1.0
    linear 2.0 xpos 2.0
    pause 1.0
    repeat
    
transform sdRunning:
    
    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.1
    ease 0.2 pos (0.48, 0.48)
    ease 0.2 pos (0.5, 0.5)
    ease 0.2 pos (0.52, 0.48)
    ease 0.2 pos (0.5, 0.5)
    repeat
    
# Зффекты   

transform sdEffect_thatgirl:

    anchor (0.5, 0.5) pos (0.5, 0.5) 
    ease 0.6 zoom 2.0
    ease 0.1 pos (0.495, 0.495)
    ease 0.1 pos (0.505, 0.505)
    ease 0.1 pos (0.505, 0.495)
    ease 0.1 pos (0.495, 0.505)
    ease 0.1 pos (0.495, 0.495)
    ease 0.1 pos (0.505, 0.505)
    ease 0.1 pos (0.505, 0.495)
    ease 0.1 pos (0.495, 0.505)
    ease 0.1 pos (0.495, 0.495)
    ease 0.1 pos (0.505, 0.505)
    ease 0.1 pos (0.505, 0.495)
    ease 0.1 pos (0.495, 0.505)
    ease 0.1 pos (0.495, 0.495)
    ease 0.1 pos (0.505, 0.505)
    ease 0.1 pos (0.505, 0.495)
    ease 0.1 pos (0.495, 0.505)

    
init 3:
    # Всё, что связано с песнями
    # Стиль песен
    $ style.sdSong = Style(style.default)
    $ style.sdSong.color = "#FFF"
    $ style.sdSong.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.sdSong.drop_shadow_color = "#000"
    $ style.sdSong.italic = True
    $ style.sdSong.bold = False
    $ style.sdSong.text_align = 0.5
    image sdSong = ParameterizedText(style = "sdSong", size = 40)
    
    # Sick Of Everyone
    $ sick_of_everyone_text1 = "В поисках ответов,\nТолько вопросы приходят на ум,\nПотому что я затерялся в кругах,\nИ, кажется, что надолго,\nИ я не знаю, как я очутился тут,\nИли даже, как я добрался до этого места,\nВсе, что я могу сказать вам, это моя судьба,\nНаписанная на черных звездах,\nНу, и что мне прикажете делать?\n\nБлагословляю себя - это мой идеальный ад,\nЛучшее, что я когда-либо знал...\nСкажите-ка мне что-нибудь такое, чего я не хочу знать,\nПотому что не могу поверить, что это действительно так.\nЧто мне прикажете делать?\n\nТеперь меня от всех тошнит,\nЯ не чувствую угрызений совести за забытое,\nИ мне на всё плевать.\nТеперь меня от всех тошнит,\nИ я всевластный голос всех проблем,\nИ мне плевать на всех."
    $ sick_of_everyone_text2 = "О, заберите меня отсюда,\nМне так все надоели.\nМне плохо, но даже так я в порядке.\nМне не нужны перемены,\nТак заберите меня отсюда!\n\nЯ падаю вниз, распавшись на части.\nТрудно сохранять целостность,\nЕсли ты не знаешь, с чего следует начать.\n\nТеперь меня от всех тошнит,\nЯ не чувствую угрызений совести за забытое,\nИ мне на всё плевать.\nТеперь меня от всех тошнит,\nИ я всевластный голос всех проблем,\nМеня от всех тошнит!"
 
# Йобаныйврот, если это когда-нибудь будет готово, это будет грандиозно!