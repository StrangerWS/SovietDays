#WIP!
label initMiniMeow:
    
    if not persistent.sdPlayMiniMeow:
        $ persistent.sdPlayMiniMeow = False
    $ sdMeowRandPlayer = "None"
    $ sdMeowRandChosen = "None"
    $ sdColorPick = "None"
    # Попался разговор с Алисой, после которого она может измениться. Необходимо положительное впечатление или статус друга.
    $ sdMeowDvBonus = False

return

label sdMiniMeowSasha:
    
    us "И... Саша!"
    if persistent.sdPlayMiniMeow == False:  
    
        sdme "Эй, почему это?"
        us "А ты ещё правил не знаешь!"
        sdme "И это повод меня первым выбирать?"
        
        show us grin pioneer with dspr
        
        us "Так же веселее!"
        "Ехидно улыбнулась Ульянка, и я понял, что мне не отвертеться."
        
    else:
    
        us "Правила повторить?"
    
    menu:
    
        "Правила":
        
            call sdMiniMeowRules
    
        "Играть":
        
            call sdMiniMeowGame
            if persistent.sdPlayMiniMeow == False:
                $ persistent.sdPlayMiniMeow = True
                
        "Пропустить игру" if persistent.sdPlayMiniMeow == True:
        
            pass
            
    show us smile pioneer at center with dissolve
    
    us "Ещё разок?"
    
    menu:
    
        "Играть":
        
            jump sdMiniMeowSasha
            
            # if renpy.random.random() > 0.167:
            
                # jump sdMiniMeowSasha
                
            # else:
                # $ sdMeowRandPlayer = renpy.random.choice(["un", "dv", "mi", "sh", "el"])
                # if sdMeowRandPlayer == "un":
                
                    # jump sdMiniMeowUn
                    
                # elif sdMeowRandPlayer == "dv":
                
                    # jump sdMiniMeowDv
                    
                # elif sdMeowRandPlayer == "mi":
                
                    # jump sdMiniMeowMi
                    
                # elif sdMeowRandPlayer == "sh":
                
                    # jump sdMiniMeowSh
                    
                # elif sdMeowRandPlayer == "el":
                
                    # jump sdMiniMeowEl
                
        "Отказаться":
            pass
            
return

label sdMiniMeowRules:

    us "Правила просты:"
    window hide
    
    $ set_mode_nvl()
    
    window show
    
    "{i}Водящий и один из игроков встают перед остальными участниками: водящий — лицом, игрок — спиной.{/i}" 
    "{i}Водящий показывает на одного из участников и спрашивает: «Кис?» Если игрок, стоящий спиной, отвечает «брысь», водящий продолжает выбирать.{/i}" 
    "{i}Как только игрок говорит «мяу», водящий спрашивает его: «Какой цвет?» Игрок выбирает цвет и участник из его команды выполняет задание.{/i}" 
    "{i}Отказаться от задания участник не имеет права.{/i}" 
    us "А теперь - цвета!"
    "{i}Белый - самый загадочный цвет. Означает \"пять минут наедине\". То есть, вы уходите на десять минут так, чтобы никто вас не видел.{/i}" 
    "{i}Зелёный - три вопроса на \"да\". То есть, ответить игрок может только \"да\".{/i}" 
    "{i}Красный - означает поцелуй в губы.{/i}"
    "{i}Розовый - поцелуй в щёчку.{/i}"
    "{i}Жёлтый - три вопроса наедине. Не ответить игрок не имеет права.{/i}"
    "{i}Оранжевый - пройтись под ручку определённый маршрут.{/i}"
    "{i}Синий - поцелуй руки.{/i}"
    "{i}Фиолетовый - три мелкие пакости.{/i}"
    "{i}Чёрный - означает \"пендель под зад\".{/i}" 
    
    window hide
    
    $ set_mode_adv()
    
    sdme "Понял."
    us "Тогда поехали!"
    
jump sdMiniMeowGame
    
label sdMiniMeowGame:
    
    show us smile pioneer at center with dissolve
    
    "Я вышел к Ульяне и повернулся спиной к окружающим."
    "Игра началась."
    
jump sdMiniMeowLoop

label sdMiniMeowLoop:

    us "Кис?"
    
    menu:
    
        "Брысь!":
        
            jump sdMiniMeowLoop
            
        "Мяу!":
        
            us "И ваш цвет..."
            
            call sdMiniMeowColor
            show effect_colorOverlayMeow
            play sound sdConfirm
            $ renpy.pause(0.25)
            hide effect_colorOverlayMeow with dspr
            hide us with dissolve
            jump sdMiniMeowDvChosen
            
            # $ sdMeowRandChosen = renpy.random.choice(["un", "dv", "mi", "sh", "el"])   
            # if sdMeowRandChosen == "un":
            
                # jump sdMiniMeowUnChosen
                
            # elif sdMeowRandChosen == "dv":
            
                # jump sdMiniMeowDvChosen
                
            # elif sdMeowRandChosen == "mi":
            
                # jump sdMiniMeowMiChosen
                
            # elif sdMeowRandChosen == "sh":
            
                # jump sdMiniMeowShChosen
                
            # elif sdMeowRandChosen == "el":
            
                # jump sdMiniMeowElChosen

label sdMiniMeowColor:

    menu:
    
        "Белый":
        
             $ sdColorPick = "white"
            
        "Зелёный": 
        
            $ sdColorPick = "green"
            
        "Красный":
        
            $ sdColorPick = "red"
            
        "Розовый":
        
            $ sdColorPick = "pink"
            
        "Жёлтый":
        
            $ sdColorPick = "yellow"
            
        "Оранжевый":
        
            $ sdColorPick = "orange"
            
        "Синий":
        
            $ sdColorPick = "blue"
            
        "Фиолетовый":
        
            $ sdColorPick = "purple"
            
        "Чёрный":
        
            $ sdColorPick = "black"
            
return
    
    
label sdMiniMeowDvChosen:

    "Передо мной стояла Алиса."
    
    if sdColorPick == "black":
    
        show dv grin pioneer with dissolve
    
        sdme "Не-е-ет. Это негуманно и неприлично."
        dv "Что, кишка тонка? Боишься, что я отвечу?"
        sdme "Да ничего я не боюсь!"
        dv "Тогда давай!"
        
        show dv normal pioneer with dspr
        
        "Алиса демонстративно повернулась ко мне... {w}спиной."
        dv "Давай, Александр! Такого шанса у тебя больше не будет!"
        "Я посмотрел на неё, на окружающих и заметил взгляд Лены."
        th "Видимо, она должна была быть на её месте."
        "Пока я стоял и мешкал, Ульянка разогналась и..."
        
        show us laugh pioneer at right
        show dv angry pioneer at left 
        with dissolve 
        play sound sfx_body_bump
        with hpunch
        with vpunch
        play music music_list["doomed_to_be_defeated"]
        
        "Со всей скорости врезалась в отставленную Двачевской мишень."        
        dv "Ах ты!.."
        dv "А ну иди сюда, мелкая!"
        "Все повалились со смеху."
        
        show us laugh pioneer:
            linear 1.0 xpos 2.0
        $ renpy.pause(0.3)
        show dv angry pioneer:
            linear 1.5 xpos 2.0
        $ renpy.pause(0.5)
        show us laugh pioneer at sdRunningchar
        $ renpy.pause(0.5)
        show dv angry pioneer at sdRunningchar
        
        "Алиса и Ульянка носились по площади, как угорелые, пока в итоге догоняющая не свалилась на лавку рядом с остальными."
        
        show dv guilty pioneer at center with dissolve 
        hide us
        stop music fadeout 3
        
        dv "Я тебе это так просто не оставлю!"
        "Прокричала Двачевская Ульянке."
        "Та в ответ показала язык." 
        "Просмеявшись, мы продолжили."
        
        hide dv with dissolve
        
    elif sdColorPick == "white":
        
        show dv shy pioneer with dissolve
        
        "Она покраснела, после чего развернулась и пошла куда-то в сторону, махнув мне рукой."
        "Я не понял её намёка."
        us "Чего встал, беги за счастьем своим!"
        "Усмехнулась Ульянка."
        "Деваться было некуда, и вскоре я поравнялся с Алисой."
        "Впервые я видел Алису... смущённой?"
        sdme "Эй, ты чего?"
        
        show dv surprise pioneer with dspr
        
        dv "В смысле?"
        sdme "Да ты красная вся!"
        
        show dv shy pioneer with dspr
        
        dv "Ты знаешь, что этот цвет значит?"
        sdme "Нет."
        "Честно признался я."
        dv "Когда ты выбираешь белый цвет, ты уходишь с человеком на десять минут..."
        sdme "Да, я это слышал."
        dv "...А они в это время сидят и обсуждают вас! И кто их знает, что взбредёт им в голову!"
        
        scene bg ext_house_of_dv_day
        show dv shy pioneer
        with dissolve
        
        "Мы остановились около очередного домика."
        dv "Сейчас пройдёт время и мы вернёмся. Здесь следить точно не будут."
        sdme "А могут?"
        
        show dv grin pioneer with dspr
        
        dv "Могут!"
        
        show blink
        $ renpy.pause(1)
        show dv shy pioneer with dspr
        hide blink
        show unblink
        
        "Через несколько минут безмолвной паузы Алиса подала голос."
        dv "Боюсь представить, что там сейчас думают."
        sdme "Пусть думают, что хотят! Каждый мыслит в меру своей испорченности."
        
        show dv laugh pioneer with dspr
        
        dv "О-о-ой, посмотрите на него, мудрейший философ Совёнка! Пошли лучше обратно."
        sdme "И всё?"
        
        show dv grin pioneer with dspr
        
        dv "А ты чего ждал? Что я разденусь тут для тебя? Иди давай!"
        "Она толкнула меня в спину, и я чуть не повалился на землю."
        
        scene bg ext_square_day with dissolve
        
        "Игра продолжилась."
        
    elif sdColorPick == "green":
        
        show dv grin pioneer with dissolve
        
        dv "Ну давай, давай."
        "Я замешкался."
        th "И что мне у неё спрашивать? \"Ты - юная террористка?\", \"Тебя вербовали мусульмане?\""
        "Прикинув, что мне за это будет, я решил ограничиться более житейскими вопросами."
        sdme "Тебя роняли в детстве?"
        
        show dv angry pioneer with dspr
        play music music_list["that_s_our_madhouse"]
        
        dv "ЧТО?!"
        "Все рассмеялись."
        us "Алиса, помни правила!"
        "Сквозь смех проговорила Ульяна."
        dv "Это я сейчас кого-то уроню!"
        sdme "А ты что думала, тебя все тут бояться будут?"
        
        show dv rage pioneer with dspr
        
        dv "ДА!"
        "Сказала Алиса, подбираясь ко мне."
        "Я медленно пятился назад, оглядываясь, чтобы не упасть."
        sdme "Считала, что так тебя будут уважать?"
        dv "ДА!"
        "Я не выдержал натиска и всё-таки споткнулся."
        
        
        play sound sfx_body_bump
        with vpunch
        scene bg ext_sky with dspr
        
        "Алиса, видимо, тоже не ожидавшая такой быстрой капитуляции, навалилась сверху."
        
        show dv angry pioneer close:
            truecenter
            zoom 1.3
        
        "Я, недолго думая, схватил её, удерживая её руки по швам, что давало мне шанс уйти от повреждений."
        dv "Отпусти!"
        
        if ptsdv >= 12 or impression >= 70:
        
            sdme "Отпущу, если успокоишься и не будешь конечностями размахивать."
            
            show dv shy pioneer close with dspr:
                truecenter
                zoom 1.3
            stop music fadeout 3
            
            dv "Саш, отпусти, пожалуйста."
            sdme "Извини. Не обижайся, это просто игра."
            dv "Я понимаю."
            
        scene bg ext_square_day with dissolve 
            
        "Мы поднялись на ноги."
            
        show dv angry pioneer with easeinbottom
            
        dv "А теперь - посмотрим, кому жизнь дорога!"
        
        if ptsdv >= 12 or impression >= 70: 
        
            "Я вздохнул и сел на бордюр, который повлёк наше падение."
            sdme "Нет."
            dv "Тебе не страшно?"
            sdme "Ничуть."
            
            show dv surprise pioneer close with dspr
            $ sdMeowDvBonus = True
            
            "Алиса удивилась, потом пришла в себя и села рядом."
            "Я был уверен, что нас никто не слышит, поэтому позволил себе немного нотаций."
            sdme "Не надо на всех реагировать, как на врагов. Никто здесь не пытается тебя опозорить и выставить дурой."
            dv "Тогда зачем было это говорить?"
            sdme "Я знал, что это выведет тебя. Опять начнёшь угрожать."
            "Алиса всё ещё с удивлением смотрела на меня."
            
            show dv guilty pioneer close with dspr
            
            dv "Может, ты и прав."
            "Видимо, Алиса тоже поняла, что мы слишком далеко, чтобы слышать наш разговор."
            "Иначе она бы никогда не признала мою правоту."
            sdme "Злишься?"
            dv "Нет. Обидно немного, но не злюсь."
            sdme "За что обидно?"
            dv "Наверное, что так со всеми обращаюсь."
            sdme "Ладно. Пошли дальше играть."
        
            show dv grin pioneer with dspr
        
            "Рыжая бестия поднялась на ноги и, повысив голос, сказала:"
        
        else:
            
            "Я продолжил пятиться, уже гораздо тщательнее выбирая путь."
            sdme "Тихо, тихо, не кипятись так. Это же просто шутка."
            dv "Я тебе сейчас покажу шутку!"
            sdme "У всех на глазах?"
            window hide
            
            show dv surprise pioneer with dspr
            $ renpy.pause(1)
            show dv angry pioneer with dspr
            
            window show
            "Это не очень помогло остановить мою участь."
            dv "Ах ты похотливый ублюдок!"
            th "Ну всё, прощай жестокий мир!"
            "В голове проносились мысли, как можно было бы успокоить разъярённого зверя, как вдруг я упёрся спиной во что-то."
            "Чем-то оказался памятник Генде."
            th "Товарищ, ты так много сделал для партии! Помоги же и мне!"
            "Не знаю, сработало это или нет, но в итоге Алиса остановилась сама."
            
            stop music fadeout 3
            show dv grin pioneer with dspr
            
            dv "Ладно, пока что прощаю."
            "Я был в шоке. Что это на неё нашло? Генда?"
            "Алиса продолжила:"
        
        dv "Но не думай, что так просто отделаешься!"
        sdme "Да-да-да."
        "Вздохнув, проговорил я."
        "Мы вернулись обратно."
        
        hide dv with dissolve
    
    elif sdColorPick == "red":
    
        "WIP"
        $ ptsun -= 1 * mulun
        $ ptsdv += 2 * muldv
    
    elif sdColorPick == "pink":
    
        "WIP"
        $ ptsdv += 1 * muldv
    
    elif sdColorPick == "yellow":
    
        "WIP"
    
    elif sdColorPick == "orange":
    
        "WIP"
    
    elif sdColorPick == "blue":
    
        "WIP"
    
    elif sdColorPick == "purple":
    
        "WIP"
    
return

label sdMiniMeowElChosen:

    "Передо мной стоял Электроник."

    if sdColorPick == "black":
     
        "WIP"
       
    elif sdColorPick == "white":
    
        "WIP"
    
    elif sdColorPick == "green":
     
        "WIP"
       
    elif sdColorPick == "red":
     
        "WIP"
       
    elif sdColorPick == "pink":
    
        "WIP"
        
    elif sdColorPick == "yellow":
     
        "WIP"
       
    elif sdColorPick == "orange":
     
        "WIP"
       
    elif sdColorPick == "blue":
     
        "WIP"
       
    elif sdColorPick == "purple":
    
        "WIP"
    
return

label sdMiniMeowMiChosen:

    "Педедо мной стояла Мику."

    if sdColorPick == "black":
        
        "WIP"
    
    elif sdColorPick == "white":
    
        "WIP"
    
    elif sdColorPick == "green":
        
        "WIP"
    
    elif sdColorPick == "red":
        
        "WIP"
        $ ptsmi += 2 * mulmi     
    
    elif sdColorPick == "pink":
        
        "WIP"
        $ ptsmi += 1 * mulmi
    
    elif sdColorPick == "yellow":
        
        "WIP"
    
    elif sdColorPick == "orange":
        
        "WIP"
    
    elif sdColorPick == "blue":
        
        "WIP"
    
    elif sdColorPick == "purple":
    
        "WIP"
    
return

label sdMiniMeowShChosen:

    "Передо мной стоял Шурик."

    if sdColorPick == "black":
        
        "WIP"
    
    elif sdColorPick == "white":
    
        "WIP"
    
    elif sdColorPick == "green":
        
        "WIP"
    
    elif sdColorPick == "red":
        
        "WIP"
    
    elif sdColorPick == "pink":
        
        "WIP"
    
    elif sdColorPick == "yellow":
        
        "WIP"
    
    elif sdColorPick == "orange":
        
        "WIP"
    
    elif sdColorPick == "blue":
        
        "WIP"
    
    elif sdColorPick == "purple":
    
        "WIP"
    
return

label sdMiniMeowUnChosen:

    "Передо мной стояла Лена."

    if sdColorPick == "black":
        
        "WIP"
    
    elif sdColorPick == "white":
    
        "WIP"
    
    elif sdColorPick == "green":
        
        "WIP"
    
    elif sdColorPick == "red":
        
        "WIP"
        $ ptsdv -= 1 * muldv
        $ ptsun += 2 * mulun
    
    elif sdColorPick == "pink":
        
        "WIP"
        $ ptsun += 1 * mulun
    
    elif sdColorPick == "yellow":
        
        "WIP"
    
    elif sdColorPick == "orange":
        
        "WIP"
    
    elif sdColorPick == "blue":
        
        "WIP"
    
    elif sdColorPick == "purple":
    
        "WIP"
    
return
