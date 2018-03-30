label sdUvao_1day:
    scene bg int_musclub_night
    play sound sfx_bush_leaves
    $ uvao_1day = True
    
    "Вдруг я услышал странный шорох."
    
    show mi scared pioneer with dissolve
    
    mi "Кто там?"
    sdme "Да наверняка кто-нибудь шарится. Сейчас посмотрю."
    
    scene bg ext_musclub_night with dissolve
    play music scarytale   
    
    "На улице никого не было. Более того, было ощущение, будто весь лагерь вымер."
    "Теперь и мне стало страшно."
    
    play sound sfx_bush_leaves
    
    "Снова шорох. Уже совсем рядом."
    "Я бросился в клуб."
    
    scene bg int_musclub_night with dissolve
    show mi scared pioneer with dissolve
    
    mi "Что там? Что ты видел?"
    sdme "..."
    mi "Саша, пожалуйста, не молчи!"
    sdme "Н-н-ничего не видел. Там никого нет."
    mi "Но что тогда шуршит?"
    sdme "Не знаю. Звук был совсем рядом."
    
    stop music fadeout 4
    
    "Мерзкий холодок пробежал по спине."
    
    play music music_list["miku_song_flute"]
    
    #Тут должен быть нормальнцый ЦГ с Мику
    show mi scared pioneer close with dspr 
    $ ptsmi += mulmi * 1
    
    "Мику внезапно бросилась на меня."
    "Всё её тело дрожало от страха, сама она вжалась в меня с такой силой, будто я единственный, кто мог её защитить в этот момент."
    sdme "Ну-ну, Мику. Успокойся. Всё нормально. Ты что, правда думаешь, что тут что-то может нам навредить?"
    
    stop music
    play sound sfx_bodyfall_1
    
    "Я услышал, как кто-то кубарем скатился за дверью и залился хохотом."
    
    scene bg ext_musclub_verandah_night with dissolve
    show mi surprise pioneer close at fright with dissolve
    show dv laugh pioneer2 at left with dissolve
    play ambience ambience_camp_center_night
    play music music_list["always_ready"] fadein 2
    
    sdme "Алиса?.."
    sdme "Так это ты тут людей пугаешь?!"
    dv "Да вы бы видели себя! \"Оно было рядом!\", \" Нам ничто не навредит!\""
    
    show mi shy pioneer with dspr
    
    "Только сейчас я заметил, что всё это время обнимал Мику за талию. После слов Алисы она отстранилась и смутилась."
    "Я тоже почуствовал, что мои щёки загорелись, и не стал удерживать девочку около себя."
    sdme "Ты что тут делаешь?"
    
    show dv grin pioneer2 with dspr
    
    dv "Да так... За влюблёнными парочками слежу! Что же мне ещё тут делать?"
    sdme "Какими парочками, ты что, с дуба рухнула?"
    
    show dv shocked pioneer2 with dspr
    stop music fadeout 4
    $ renpy.pause(1, hard = True)
    show dv normal pioneer2 with dissolve
    
    "Я, видимо, был настолько зол, что Алиса решила перейти на серьёзный тон."
    dv "Ладно, просто мимо проходила, услышала музыку, решила поближе подойти."
    
    show dv laugh pioneer2 at left with dissolve
    
    dv "А там вы... Обнимаетесь."
    "Я решил пропустить её последнее слово мимо ушей."
    sdme "Разве тебя не должны держать под домашним арестом?"
    
    show dv grin pioneer2 with dspr
    
    dv "У меня есть хорошие друзья!"
    "Рассмеялась она и ушла."
    
    hide dv with dissolve
    show mi normal pioneer at center with ease
    
    th "Да, первый день в лагере, а уже слухи."
    sdme "Как думаешь, она расскажет кому-нибудь?"
    mi "О чём?"
    sdme "О том, что она видела."
    
    show mi shy pioneer close with dspr
    play music music_list["miku_song_flute"]
    
    "Мику внезапно подошла и обняла меня." 
    "Видимо, это было внезапно и для неё самой, потому что она тут же покраснела."
    sdme "Ты чего?"
    
    show mi smile pioneer close with dspr

    "Поначалу Мику ничего не ответила, затем, придя в себя, сказала:"
    mi "А что такого в том, что два человека обнялись?"
    "Я удивился."
    th "Ну не может же быть такого, чтобы я ей за один день понравился!"
    th "Хотя... Действительно, что такого?"
    
    if ptsdv >= 2:
    
        th "Как будто я хочу перед Алисой оправдаться!"
        
    th "Да и в принципе она довольно привлекательная. Если бы у нас что-то вышло, я бы не был против."
    "Мику вывела меня из транса."
    mi "Саша, это неприлично. Даме положено отвечать."
    "Она надула губки и разжала объятья."
    
    show mi smile pioneer with dspr
    
    sdme "Честно говоря, не знаю. Просто всегда думаю о том, что творится в голове у других."
    mi "А у тебя в голове что творится?"
    sdme "Я считаю, что это просто испуг. Или дружеские объятья."
    th "Хотя, до друзей нам ещё далеко. {w}Или нет..."
    "Мику кивнула, осмотрелась вокруг и вдруг перешла на более серьёзный тон."
    
    show mi normal pioneer with dspr
    
    mi "Слушай, Саш, уже поздно. Давай на сегодня закончим?"
    sdme "И правда. Да, давай. Завтра продолжим, если меня не займут."
    
    show mi smile pioneer with dspr
    
    mi "Ну, тогда увидимся на линейке. Пока!"
    
    hide mi with dissolve
    
    "И она тут же скрылась за поворотом."
    "Так легко и невозмутимо, как будто и не было никаких шорохов, страхов..."
    
    stop music fadeout 4
    
    "А я стоял с диким недопониманием в своей голове."
    th "Что {w=.5}сейчас {w=.5}было?"
    th "Разве не парень должен приставать к девушкам?"
    "Я усмехнулся."
    
    scene bg ext_musclub_night with dissolve
    
    "Как бы там ни было, я ощущал дикую усталость в своём теле, поэтому вяло зашагал к своему домику."
    
    play sound sfx_bush_leaves
    play music music_list["no_tresspassing"] fadein 2
    
    "Как вдруг..."
    "Это была явно не Алиса. {w}И не Мику."
    "Я ощутил всё тот же мерзкий холодок. {w}Только на этот раз он бежал не по спине, а окутывал меня со всех сторон."
    "Туман будто усилился."
    "Я со всех ног побежал к нашему домику."
    
    scene bg ext_houses_night with dissolve
    show mi surprise pioneer at center with dissolve 
    stop music fadeout 5
    
    "Я умудрился догнать Мику на аллее и здорово её перепугать."
    sdme "Не смотри так на меня. Я просто..."
    sdme "Там кто-то следит за мной!"
    
    show mi scared pioneer with dspr
    
    mi "Я надеюсь, ты шутишь?"
    sdme "Я бы сам ужасно хотел. Но нет."
    "Мику тут же побледнела."
    
    play soundloop sfx_far_steps
    
    "Вдруг послышались шаги."
    "Впереди кто-то появился и медленно вышел на свет."
    
    show mi scared pioneer at left with ease
    show mz bukal glasses pioneer far at right with Dissolve(2)
    stop soundloop
    
    "Я выдохнул, когда свет озарил лицо Жени."
    mz "А вы чего не на площади? Все вроде уже там."
    mz "Господи, ребят, что случилось? Вы все бледные!"
    mi "З-з-за нами кто-то с-с-сле..."
    sdme "Стой, Мику. Давай не будем паниковать." 
    
    show mi normal pioneer with dspr
    show mz bukal glasses pioneer with dissolve
    
    "Я тряхнул головой, и моё лицо приняло невозмутимое выражение."
    "Мне стало как-то спокойнее, когда рядом появилась сестра."
    sdme "Ещё раз проанализируем. Мы услышали шорохи в кустах."
    sdme "Самые обычные, которые может создать любое живое существо."
    sdme "И по воле случая мы приняли это за человека."
    mz "Хм-м-м... Я тоже слышала шорохи."
    sdme "ЖЕНЯ! Я пытаюсь успокоиться!"
    
    show mz laugh glasses pioneer with dspr
    
    mz "Не паникуй, братик. У тебя мания величия. Это просто ветер."
    
    show mz normal glasses pioneer with dspr
    
    mz "Пошли уже, а то Славя только вас и ищет."
    
return