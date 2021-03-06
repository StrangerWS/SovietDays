# ================================================================================== #
#                   ОФИЦИАЛЬНАЯ ДОКУМЕНТАЦИЯ ФАЙЛА СЦЕНАРИЯ                          #
# ================================================================================== #
# Файл сценария мода «Советские будни».                                              #
# Разработчик — StrangerWS, 2015-2020.                                               #
# ВСЕ ДАННЫЕ, ИСПОЛЬЗОВАННЫЕ В ЭТОМ МОДЕ, ПРИНАДЛЕЖАТ ИХ ПЕРВИЧНЫМ ПРАВООБЛАДАТЕЛЯМ! #
#    АВТОР МОДА НЕ НЕСЁТ ОТВЕТСТВЕННОСТИ ЗА ДАЛЬНЕЙШЕЕ РАСПРОСТРАНЕНИЕ МАТЕРИАЛОВ!   #
# ================================================================================== #

init:
    $ filters["sdPlayMod"] = u"(Альфа) Советские Будни"

    # Инициализируем все данные, с которыми будем работать.

    call initVars       # Переменные мода
    call initChars      # Персонажи
    call initImg        # Картинки
    call initSnd        # Звуки, музыка
    call initMiniMeow   # Переменные мини-игры

# Для тестеров!
label sdTests:
    stop music fadeout 2
    hide screen sdMenu
    with fade
    scene bg black

    $ set_mode_nvl()
    window show

    $ persistent.sprite_time = "prolog"
    $ prolog_time()

    menu:

        "Первый день. ЮВАО-кусок.":

            $ set_mode_adv()
            $ persistent.sprite_time = "night"
            $ night_time()
            jump sdUvao_1day

        "ЮВАО-рут":

            $ set_mode_adv()
            $ persistent.sprite_time = "day"
            $ day_time()
            jump sdUvRoute

        "Мини-игры: Кис-мяу":

            $ set_mode_adv()
            $ persistent.sprite_time = "day"
            $ day_time()
            scene ext_square_day with dissolve
            show us smile pioneer with dissolve
            jump sdMiniMeowSasha

        "Тест Меню виджетов":

            jump sdWidgetMenu



        "Выход в главное меню мода":

            window hide
            show screen sdMenu
            with fade2
            play music five_years fadein 3
            $ renpy.pause(hard = True)

label sdPrepare:

# Инициализация переменных, которые должны проинициализироваться только один раз.
    call initMap

    stop music fadeout 2
    hide screen sdMenu
    with fade

    $ set_mode_adv()
    $ sdStart = True
    $ sd_chapter(1, u"Предыстория.")
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    scene black
    $ renpy.pause(3, hard = True)
    scene anim prolog_1 with fade3
    
    "Беззаботное и весёлое советское время… {w}Самое запоминающееся время в моей жизни." 
    "Нет, я не тот, кто кричит, что в СССР было лучше."
    "Просто в это время прошла моя юность."
    "И помню, как сейчас, мои семнадцать…"

    scene bg ext_city_day with dissolve

    "Я родился в тихом советском городишке далеко от райцентра, настолько неизвестном, что время стёрло его название с карт СССР."
    "Да и не имеет это никакого значения."
    "В семье нас было двое — я и моя младшая сестра, Женя."
    "Мы были обычными советскими детьми, все, как один, мечтали стать пионерами и космонавтами."
    "Мой школьный друг Сергей, взявший себе кличку «Электроник», всё детство провёл вместе с нами."
    "Мы сидели с ним за одной партой, порой, прогуливали занятия, чтобы попинать мячик во дворе."
    "В нашей семье Электроника принимали как родного. Его ждали всегда — и на Новый год, и на масленицу, и на Первомай — в общем, место за нашим столом для него всегда было."

    stop music fadeout 4
    
    "Время шло, мы взрослели…"
    
    scene bg int_classroom_day with dissolve
    play music music_list["everyday_theme"]
    
    "В последние дни учёбы наш учитель разложил у себя на столе несколько листов с путёвками в разные лагеря." 
    "Все тут же весёлой гурьбой налетели занимать места. Я же сидел и наблюдал за этим ажиотажем, царившим у стола Анатолия Михайловича."
    "Я в лагерях никогда не был - скучно это, если одному ехать, а за Женей следить надо - я же, хоть и на год, но старше."
    "Первым из толпы вынырнул Электроник."
    
    show el smile pioneer with dissolve

    el "Сань, а ты чего? В лагерь не хочешь?"
    sdme "Не знаю... Ещё не нашёл подходящих вариантов."

    show el surprise pioneer with dspr

    el "Так иди, посмотри на списки, может, на месте и решишь."
    "Вдруг у Электроника промелькнула какая-то мысль."

    show el smile pioneer with dspr

    el "Слушай, а поехали со мной в Совёнок! И Женьку возьми, что дома тухнуть будет?"
    th "А что, вместе же веселее... Может, съездить?"
    sdme "А давай!"

    hide el with dissolve

    "Я пробился сквозь толпу и крикнул:"
    sdme "Анатолий Михайлович, места в Совёнок остались?"
    "Учитель кивнул мне."
    sdme "Запишите ещё два!"

    scene bg ext_backyard_day with dissolve
    stop music fadeout 4    
    
    "Дома я рассказал родителям про эту затею." 
    "Они приняли её довольно тепло и даже порадовались, что мы с сестрой познаем все прелести пионерлагеря."
    "Да и Женя была в эйфории, предвкушая новые знакомства и развлечения."
    
    jump sdChoose