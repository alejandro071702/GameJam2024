label iotDay2:
    scene bg_mono_micro with circlewipe
    show iot feliz at left with sr_easein
    show negro as negro1 at slightright
    show negro as negro2 at right
    iot "Recuerda que el pin que necesitamos el cuarto pin."
    "" "..."
    iot "Termina la tabla de registro."
    p "..."
    iot "¿No crees que los ticks del reloj van muy rápido?"
    "" "Si quieres que quede tan perfecto, ¿porqué no haces todo tú en lugar de mandonearnos?"
    "" "Nosotros ya hicimos suficiente."
    show iot troste at left
    hide negro1 with moveoutright
    hide negro2 with moveoutright
    p "..."
    show iot troste at center with move
    iot "... ¿Porqué no te fuiste?"
    menu: 
        '¿A poco el salón es tuyo?':
            show iot molesto at center
            iot "... Pues no, pero no tienes que ser tan grosero."
        'Repruebo si no hago la práctica':
            show iot molesto at center
            iot "Entonces no te importan mis sentimientos."
            # iot "Bueno, supongo que cualquier razón es buena."
        'No puedo abandonarte a tu suerte para terminar la práctica':
            show iot molesto at center
            iot "¿No me crees capaz de hacer esto por mi cuenta? Eso es aún más insultante que lo que hicieron los demás."
            # "" ""
    play sound "punch.opus"
    $ HideInterface()
    scene black with circleirisoutfast
    hide iot molesto
    pause(4.0)
    $ renpy.movie_cutscene("intro.webm")
    return
            

    
