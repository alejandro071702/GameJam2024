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

$ renpy.music.register_channel(channel1, loop=True)
$ renpy.music.register_channel(channel2, loop=True)
init:
    image iot feliz = Composite(
        (320, 320),
        (0, 0), "mona1.png",
        (119, 119), "face feliz.png")
    
    define circirisout = ImageDissolve("circleiris.png", 1.0, time_warp=_warper.easeout)
    define circirisin = ImageDissolve("circleiris.png", 1.0, reverse=True, time_warp=_warper.easein)

label start:
    jump charPlayground
    return
    jump inicio

label inicio:
    scene black
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Vato123"
        p = Character("[name]", color = "#FFF")
    
    p "Llevo cinco semestres estudiando una Ingeniería en Computación y no tengo ni la menor idea de lo que estoy haciendo."
    p "Creo que todo el tiempo que pasé en la escuela lo hice en piloto automático. Menos mal que sabía cuáles eran los profesores barcos."
    p "Estoy por comenzar el sexto semestre. Tengo que elegir un área de énfasis al siguiente y no sé qué se hace en cada una más allá de lo que podría adivinar por sus nombres."

    scene salon
    p "No es que mis calificaciones sean malas, aunque son apenas pasables. Pero estoy completamente seguro que no podré titularme."
    p "… en especial cuando no sé qué elegir para enfocarme."
    p "Espero que las clases que tomaré este semestre me ayuden a decidir."
    p "…"
    p "Que sea lo que Dios quiera."
 
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    menu:
        "Show example":
            jump example
        "Exit":
            return

    return

label example:
    scene bg micro
    show geo angry
    geo "Baka mou shiranai"

    scene black with Dissolve(0.5)
    pause(0.5)

    scene bg micro
    show iot happy 
    show img pe behind iot
    p "..."
    narrator "Narration"
    narrator "A long time ago..."
    with Dissolve(0.5)

    return

label charPlayground:
    scene bg micro
    show iot feliz
    iot "Hola"
    return


label transitionPlayground:
    scene micro-bg
    pause(2.0)
    scene black with circirisin
    pause(2.0)
    scene salon with circirisout
    pause(2.0)
