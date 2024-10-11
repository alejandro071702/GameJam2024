# Coloca el código de tu juego en este archivo.

# Characters
define iot = Character('Chipi-Chan', color = "#BEA665")
define cloud = Character('Nubeka', color = "#004B8B")
define web = Character('S/N', color = "#000000")
define geo = Character('Mappu', color = "#FFF")

#Narrator
define narrator = Character(kind = nvl)

#Player
define p = Character('Vato123')

# El juego comienza aquí.
define circleirisin = ImageDissolve("imagedissolve circleiris.png", 1.0, 8 , reverse=True)
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define circlewipe = ImageDissolve("imagedissolve circlewipe.png", 1.0, 8)
define sl_easein = MoveTransition(1.0, enter=offscreenleft, enter_time_warp=_warper.easein)
define sr_easein = MoveTransition(1.0, enter=offscreenright, enter_time_warp=_warper.easein)

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

$ renpy.music.register_channel(channel1, loop=True)
$ renpy.music.register_channel(channel2, loop=True)
init:
    image cloud feliz = Composite(
        (600, 600),
        (0, 0), "mona1.png",
        (250, 265), "face feliz.png"
    )

    image web feliz = Composite(
        (600, 600),
        (0, 0), "mona2.png",
        (250, 265), "face feliz.png"
    )

    image geo feliz = Composite(
        (600, 600),
        (0, 0), "mona3.png",
        (250, 265), "face feliz.png"
    )


label char:
    scene micro-bg
    show iot feliz
    iot "Hola"
    return

label start:
    jump inicio
    return

label showlogo:

    return

label inicio:
    play music "test one.ogg" fadeout 1
    scene black with Dissolve(0.5)
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Vato123"
        p = Character("[name]", color = "#FFF")
    
    p "Llevo cinco semestres estudiando una Ingeniería en Computación y no tengo ni la menor idea de lo que estoy haciendo."
    p "Creo que todo el tiempo que pasé en la escuela lo hice en piloto automático. Menos mal que sabía cuáles eran los profesores barcos."
    p "Tengo que elegir un área de énfasis al siguiente y no sé qué se hace en cada una más allá de lo que podría adivinar por sus nombres."
    p "Espero que pueda tomar una decisión para el final de este semestre..."

    scene bg_pasillo with Dissolve(0.5)
    p "Aunque, antes de eso… tal vez ni siquiera alcance a pasar este semestre. Llevo la mitad del sexto semestre reprobando todas las materias. "
    p "Al menos mantengo la esperanza de recuperarme los siguientes parciales."
    p "Estoy completamente seguro que no podré titularme a este paso."
    p "…"
    p "Que sea lo que Dios quiera."

    # jump showlogo

    p "Creo que es hora de ir a mi primera clase."

    scene bg_redes with Dissolve(0.5)
    scene black with circlewipe
    # pause(1.0)
    scene bg_redes with circlewipe

    p "(Las clases se sienten más pesadas cuando intentas prestar atención. Ni siquiera sé si me quedó todo claro)"

    show cloud feliz with sl_easein

    p "(Esta es la chica que se sienta al lado mío, cloudGirl. Estábamos juntos en un equipo hace unos semestres, pero nunca la vi hablar; sólo envió su parte del trabajo al final, y fue lo mejor de todo el proyecto.)"
    p "(Nunca le había hablado… Tal vez pueda ayudarme a pasar)."
    p "Oye… ¿entendiste la clase?"
    cloud "Sí."
    p "(Así que sí puede hablar)."
    p "Me perdí un poco, ¿podrías explicarme?"
    cloud "La capa de transporte en el modelo OSI se encarga de segmentar y reensamblar la información para transmitirla de manera eficiente. A cada segmento se le asigna un número de secuencia para que el receptor pueda rehacerlos en el orden correcto. Utiliza protocolos de control como TCP para asegurar que todos los paquetes lleguen-"

    hide cloud feliz

    "" "..."

    #return


label c2:
    scene bg_pasillo
    p "Al menos estoy seguro de que puedo pedirle ayuda..."
    p "Hora de mi siguiente clase"
    "Profesor" ``

    show geo feliz at right with sl_easein
    show web feliz at left with sr_easein

    geo ""

label microcontroladores:
    scene bg_mono_micro
    'Profesor' "Así tiene que quedar su proyecto. Es en equipos, y para no complicarnos las cosas, trabajen con la persona que sigue de ustedes en la lista."
    p "(Después de mí… Supongo que me toca con ella)"

    return


label example:
    scene micro-bg
    show geo angry
    geo "Baka mou shiranai"

    scene black with Dissolve(0.5)
    pause(0.5)

    scene micro-bg-2
    show img pe:
        xalign 0.0
        yalign 1.0

    p ""
    show img pe:
        xpos 1.0
        ypos 1.0
    narrator "Narration"
    narrator "A long time ago..."
    with Dissolve(0.5)

    return
