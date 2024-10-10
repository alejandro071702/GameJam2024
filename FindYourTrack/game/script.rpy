# Coloca el código de tu juego en este archivo.

# Characters
define iot = Character('Chipi-Chan', color = "#BEA665")
define cloud = Character('Nubeka', color = "#004B8B")
define web = Character('S/N', color = "#000000")
define geo = Character('Mappu', color = "#FFF")

#Narrator
define narrator = Character(kind = nvl)

# El juego comienza aquí.
define circleirisin = ImageDissolve("imagedissolve circleiris.png", 1.0, 8 , reverse=True)

define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
 
 


label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg micro

    show geo angry

    geo "Baka mou shiranai"

    scene black
    with circleirisin

    scene bg micro
    show img pe:
        xalign 0.5
        yalign 0

    pause(0.2)
    show img pe:
        xalign 0.5
        yalign 1
    narrator "Narration"
    narrator "A long time ago..."
    with circleirisout

    return