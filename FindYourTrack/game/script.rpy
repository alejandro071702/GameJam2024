# Coloca el código de tu juego en este archivo.

# Characters
define iot = Character('Chipi-Chan', color = "#FFF")
define cloud = Character('Nubeka', color = "#004B8B")
define geo = Character('Mappu', color = "#FBB900")
define web = Character('Sunny', color = "#BEA665")

#Narrator
define narrator = Character(kind = nvl)

#Player
define p = Character('Vato123')
define name = 'Vato123'
# El juego comienza aquí.
define circleirisin = ImageDissolve("imagedissolve circleiris.png", 1.0, 8 , reverse=True)
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define circlewipe = ImageDissolve("imagedissolve circlewipe.png", 1.0, 8)
define sl_easein = MoveTransition(0.5, enter=offscreenleft, enter_time_warp=_warper.easein)
define sr_easein = MoveTransition(0.5, enter=offscreenright, enter_time_warp=_warper.easein)

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0
image towa_animated = Animation("images/towa front.png", 0.5, "images/towa side.png", 0.5)

# $ renpy.music.register_channel(channel1, loop=True)
# $ renpy.music.register_channel(channel2, loop=True)
init:
    image cloud feliz = Composite(
        (600, 600),
        (0, 0), "mona1.png",
        (250, 265), "face feliz.png"
    )

    image cloud bien feliz = Composite(
        (600, 600),
        (0, 0), "mona1.png",
        (250, 265), "face bien feliz.png"
    )

    image web feliz = Composite(
        (600, 600),
        (0, 0), "mona3.png",
        (250, 265), "face feliz.png"
    )
    
    image web triste = Composite(
        (600, 600),
        (0, 0), "mona3.png",
        (250, 265), "face troste.png"
    )

    image web muyfeliz = Composite(
        (600, 600),
        (0, 0), "mona3.png",
        (250, 265), "face bien feliz.png"
    )

    image web molesto = Composite(
        (600, 600),
        (0, 0), "mona3.png",
        (250, 265), "face molesto.png"
    )

    image geo feliz = Composite(
        (600, 600),
        (0, 0), "mona2.png",
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
    scene black with Dissolve(0.5)
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Player"
        p = Character("[name]", color = "#FFF")
    
    p "Llevo cinco semestres estudiando una Ingeniería en Computación y no tengo ni la menor idea de lo que estoy haciendo."
    p "Creo que todo el tiempo que pasé en la escuela lo hice en piloto automático. Menos mal que sabía cuáles eran los profesores barcos."
    p "Tengo que elegir un área de énfasis al siguiente y no sé qué se hace en cada una más allá de lo que podría adivinar por sus nombres."
    p "Espero que pueda tomar una decisión para el final de este semestre..."

    scene bg_mono_pasillo with Dissolve(0.5)
    show alpha_filter
    p "Aunque, antes de eso… tal vez ni siquiera alcance a pasar este semestre. Llevo la mitad del sexto semestre reprobando todas las materias. "
    p "Al menos mantengo la esperanza de recuperarme los siguientes parciales."
    p "Estoy completamente seguro que no podré titularme a este paso."
    p "…"
    p "Que sea lo que Dios quiera."

    # jump showlogo

    p "Creo que es hora de ir a mi primera clase."

    scene black with circlewipe
    scene bg_redes with Dissolve(0.5)
    # pause(1.0)
    play music "main track.ogg"
    #return
    jump cloud1


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
