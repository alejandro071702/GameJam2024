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
define sl_easein = MoveTransition(0.5, enter=offscreenleft, enter_time_warp=_warper.easein)
define sr_easein = MoveTransition(0.5, enter=offscreenright, enter_time_warp=_warper.easein)

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

label interfaces:
    #Día antes del examen
    scene bg_salon
    p "(Veo a todos muy preocupados, ¿olvidé hacer algún proyecto?)"
    p "(¡No puede ser! Olvidé el examen, no he estudiado nada y no creo alcanzar a ver en una noche, menos 5 minutos antes)"
    show web feliz
    web "¡Hola, user! ¿Emocionado por el examen de mañana? Llevo desvelándome toda la semana, estoy segura de que me irá bien."
    p "(Qué animada, ¿quién se alegra por un examen?) Eh... en realidad no. No he estudiado nada... y no entiendo nada."
    web "Pero no es tan difícil. Si pudiste hacer los ejercicios que encargó el profesor, no creo que tengas problema."
    p "¿Crees qué puedas explicarme más tarde? Si tienes tiempo libre."
    web "Tengo mi agenda muy apretada, pero ¡va! Te veo más tarde."
    "" "..."
    p "(Llevo esperando a Web, no la veo por ningún lado. Espero que sí venga.)"
    web "¡Hey! Perdón por la tardanza, tenía un compromiso."
    p "Está bien, no te preocupes."
    "" "..."
    p "... Ah, muchas gracias, creo que ya entiendo mejor los temas. Se nota que te gusta mucho esta materia."
    web "Síí, siempre me ha gustado mucho el diseño, dibujar y el frontend, además quiero enfocarme en el Área de Énfasis de Desarrollo Web y Multiplataforma."
    p "¿En serio? Yo aún no decido que área elegir... pero dime, ¿por qué te interesa esa en especifico?"
    web "El desarrollo web y multiplataforma es interesante por su accesibilidad global, versatilidad al funcionar en múltiples dispositivos, constante evolución tecnológica, alta demanda laboral, y por permitir creatividad en la creación de experiencias interactivas."
    p "Genial... Suena interesante, no había puesto tanta atención a lo que conlleva el área."
    web "Podría hablar todo el día, ¿quieres que siga?"
    p "Sí, por favor"
    web "Bueno, ahondando en cada característica que te mencioné, es interesante porque las aplicaciones web son accesibles desde cualquier dispositivo con conexión a Internet, lo que permite a los desarrolladores llegar a un público más amplio. De igual manera, el desarrollo multiplataforma permite crear aplicaciones que funcionen en diferentes sistemas operativos como Windows, macOS, Android e iOS con un solo código base, lo que ahorra tiempo y recursos. También, la tecnología web está en constante evolución, lo que brinda oportunidades para aprender y aplicar nuevas herramientas y frameworks, como React, Angular o Vue.js. Y una gran ventaja es que hay una alta demanda de desarrolladores web y multiplataforma en el mercado laboral, lo que significa mejores oportunidades de empleo y crecimiento profesional. Y el principal motivo por el cual me gusta es porque el desarrollo web permite la creación de experiencias interactivas y visuales, lo que estimula la creatividad y la innovación."
    p "(Ah mi mente, demasiada información para mí)" 
    p "Así cómo lo explicaste sí suena bien chevere."
    web "¿Verdad que sí?, ¿qué fue lo que te llamó la atención?"
    menu: 
        "resp_1":
            p "Me llamó la atención que las aplicaciones sean accesibles desde cualquier dispositivo con conexión a Internet."
            web "A mí también."
        "resp_2":
            p "Que será fácil conseguir trabajo."
            web "Sí, muchos lo eligen por eso."
        "resp_3":
            p "El dorado de tus ojos."
            web "Estamos hablando del desarrollo web."
    web "Aunque, tiene sus desventajas, si no tienes Internet no será funcional."
    p "(No me interesaba pra nada esa área, pero ella lo hace ver interesante)"
    " " "..."
    p "(Nos quedamos un par de horas hablando, fue muy intrigante conocer más acerca del área de desarrollo web)"
    p "(Tampoco había notado lo linda que se ve hablando de lo que la apasiona)"
    
    return

label interfaces:
    #Día al final del semestre
    scene bg_salon
    p "(Terminé todos mis exámenes finales del semestre, fue complicado, pero se logró con mucha fe. Dudo sí pasaré todas mis materias, los últimos días las descuidé un poco porque decidí enfocarme más en interfaces gráficas, ya que necesito tenerla aprobada si quiero estudiar el track de desarrollo web)."
    show web feliz
    web "¿Qué tal?, ¿cómo te fue en tus exámenes?"
    p "Me fue. Comparado a las primeras evaluaciones del semestre, creo que ha sido lo mejor que me ha ido."
    web "¡Qué bien!"
    p "Y estoy seguro que en interfaces me fue bien. Gracias a tu ayuda."
    web "Me alegro de oírlo. Aquí andamos para ayudar."
    p "También, acabé convenciéndome por estudiar el área de desarrollo web. ¿Y tú?, ¿no habrás cambiado de opinión?"
    web "Claro que no, y menos ahora que sé que estaremos juntos."
    "" "..."
    p "(Al final decidí enfocarme más en el área de Desarrollo Web y Multiplataforma, y la materia requisito para cursar dicha área es Interfaces Gráficas con Aplicaciones, así que le dediqué la mayor parte de mi tiempo y dejé de lado las otras materias y proyectos. Con mucha fe pasé mi sexto semestre)."
    p "(No me quejo. Web y yo nos hicimos más cercanos gracias a que compartimos intereses, nos ayudamos el resto del curso de interfaces y ahora estaremos juntos en el Área de Énfasis)."
    
    return

label sig_sem_web:
    scene bg_salon
    p "(Cuando tuve mi tutoría este semestre, mi profesor me preguntó cuál sería el área de énfasis que iba a escoger... en ese momento no tenía idea de cuál sería mi vocación. Ninguno me interesaba, se escuchaban muy complicados, inlcuso llegué a pensar que me había equivocado de carrera. Ahora que terminó el semestre, gracias a W, obtuve una visión más clara de mi futuro. Ahora sé que mi área es el Desarrollo Web y Multiplataforma. Me pareció interesante como las aplicaciones interactivas, el diseño de interfaces y las aplicaciones escalables son relevantes para esta área de énfasis porque permiten responder a las necesidades de los usuarios ofreciendo una experiencia fluida, eficiente y accesible para un amplio público sin importar el dispositivo que se utilice)."

    return

label sig_sem_cloud:
    scene bg_salon
    p "(Cuando tuve mi tutoría este semestre, mi profesor me preguntó cuál sería el área de énfasis que iba a escoger... en ese momento no tenía idea de cuál sería mi vocación. Ninguno me interesaba, se escuchaban muy complicados, inlcuso llegué a pensar que me había equivocado de carrera. Ahora que terminó el semestre, gracias a Z, obtuve una visión más clara de mi futuro. Ahora sé que mi área es el Cómputo en la Nube. Elegí esta área de énfasis debido a que me pareció artayente como la arquitectura en la nube y los servicios en la nube son esenciales para el cómputo en la nube porque constituyen la estructura base y los componentes clave que permiten a esta tecnología funcionar de manera eficaz, flexible y evolutiva. Esos dos elementos definen como los recursos son organizados, gestionados y proporcionados mediante la nube, garantizando que los usuarios se puedan beneficiar de estas ventajas)."

    return

label sig_sem_iot:
    scene bg_salon
    p "(Cuando tuve mi tutoría este semestre, mi profesor me preguntó cuál sería el área de énfasis que iba a escoger... en ese momento no tenía idea de cuál sería mi vocación. Ninguno me interesaba, se escuchaban muy complicados, inlcuso llegué a pensar que me había equivocado de carrera. Ahora que terminó el semestre, gracias a Y, obtuve una visión más clara de mi futuro. Ahora sé que mi área es el Internet de las Cosas. Me llamó la atención como la robótica, la automatización y el control digital son esenciales para hacer los procesos más inteligentes, autónomos y económicamente viables. Puesto que permiten a las máquinas tomar cargas de tareas complejas con mayor precisión y eficacia, estas tecnologías juegan un rol fundamental dentro del desarrollo del IoT, ya que ayudan a mejorar la gestión de recursos, seguridad y la calidad de vida)."
    
    return

label sig_sem_geo:
    scene bg_salon
    p "(Cuando tuve mi tutoría este semestre, mi profesor me preguntó cuál sería el área de énfasis que iba a escoger... en ese momento no tenía idea de cuál sería mi vocación. Ninguno me interesaba, se escuchaban muy complicados, inlcuso llegué a pensar que me había equivocado de carrera. Ahora que terminó el semestre, gracias a X, obtuve una visión más clara de mi futuro. Ahora sé que mi área son los Sistemas Geoespaciales. Me parece muy interesante como la IA y la visión computacional son esenciales, ya que permiten hacer análisis de manera rápida y eficaz de imágenes y videos para el reconocimiento, estudio, clasificación y vigilancia de los recursos naturales y suelos, además de detectar patrones y/o cambios en el medio ambiente posibilitando hacer predicciones de eventos o tendencias sobre los datos geoespaciales)."

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
