label sdActivitiesEnterLoop:
    
    "Я решил записаться в один из кружков."
    
    scene bg int_clubs_day with dissolve
    show el normal pioneer with dissolve
    
    el "О, привет, Сань. Ты чего хотел?"
    sdme "Да вот, в кружок записаться."
    el "В какой?"
    
    menu:
        "В музыкальный" if music >= 2 and not music_worker:
        
            show el grin pioneer with dspr
            
            el "Смотри, а то Мику тебе точно мозг расплавит!"
            sdme "Нет, не расплавит, я привык уже."
            
            $ music_worker = True
            $ music = 5
            
        "В медицинский" if medic >= 2 and not medic_worker:
            
            show el grin pioneer with dspr
            
            el "О-о-о, а наш Саша не так прост, как кажется! Уже и на медсестру запал!"
            sdme "Че-е-его?! Ты сейчас это серьёзно сказал?"
            el "Ой, да ладно тебе! Всё же кристально ясно!"
            sdme "Записывай давай и заканчивай с такими шуточками."
            
            $ medic_worker = True
            $ medic = 5
            
        "В ваш, конечно же!" if cyber >= 2 and not cyber_worker:
            
            show el smile pioneer with dspr
            
            el "Тогда, это, велкам, что ли!"
            sdme "Ладно, я позже зайду."
            
            $ cyber_worker = True
            $ cyber = 5
            
        "Хочу вожатой помогать" if mtmerc >= 2 and not mtmerc_worker:
            
            el "Ох, и рисковый ты, Саша. Загрузит она тебя до конца жизни!"
            sdme "В любом случае, это моя забота."
            
            $ mtmerc_worker = True
            $ mtmerc = 5
            
        "В столовую" if dining >= 2 and not dining_worker:
            
            el "А может, ты мне притащишь поесть сюда?"
            sdme "Давай, иди жир растрясать, лентяй!"
            
            $ dining_worker = True
            $ dining = 5
            
        "Забудь":
            pass

    show el normal pioneer with dspr        
    
    el "Ну хорошо."
    sdme "Увидимся."
    
return

label sdActivitiesExitLoop:

    "Я решил выйти из одного из кружков."
    
    scene bg int_clubs_day with dissolve
    show el normal pioneer with dissolve
    
    el "О, привет, Сань. Ты чего хотел?"
    sdme "Да вот, времени мало, думаю выйти из кружка."
    el "Из какого?"
    
    menu:
        "Из музыкального" if music_worker:
        
            show el sad pioneer with dspr
            
            el "А как же Мику?"
            sdme "Да она и одна справится. А поболтать всегда время будет."
            
            show el grin pioneer with dspr
            
            el "Да, с ней наболтаешься на месяц вперёд."
            
            $ music_worker = False
            
        "Из медицинского" if medic_worker:
            
            show el grin pioneer with dspr
            
            el "Что, не срослось с Виолой?"
            sdme "Серёга, ты умрёшь не своей смертью."
            el "Ой, напугал!"
            sdme "Просто вычеркни меня."
            
            $ medic_worker = False
            
        "Из вашего" if cyber_worker:

            $ cyber_worker = False
            
        "Не хочу больше вожатой помогать" if mtmerc_worker:
            
            show el grin pioneer with dspr
            
            el "Я же говорил, она тебя в могилу сгонит!"
            sdme "Ты был прав."
            
            $ mtmerc_worker = False
            
        "Из столовой" if dining_worker:
            
            show el sad pioneer with dspr
            
            el "А кто мне плюшки таскать будет?"
            sdme "Да ты посмотри на себя! И без плюшек в дверь не помещаешься!"
            
            $ dining_worker = False
            
        "Забудь":
            pass
            
    show el normal pioneer with dspr
            
    el "Ну, твоё право."
    sdme "Ладно, увидимся."

return 