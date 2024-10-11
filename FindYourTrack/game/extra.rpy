define teleport = ImageDissolve("imagedissolve teleport.png", 1.0, 0)

label extraStart:
    image extra feliz = Composite(
        (600, 600),
        (0, 0), "mona5.png",
        (250, 265), "face feliz.png"
    )
    image extra molesto = Composite(
        (600, 600),
        (0, 0), "mona5.png",
        (250, 275), "face molesto.png"
    )
    image extra troste= Composite(
        (600, 600),
        (0, 0), "mona5.png",
        (250, 265), "face troste.png"
    )
    image extra bien feliz= Composite(
        (600, 600),
        (0, 0), "mona5.png",
        (250, 265), "face bien feliz.png"
    )

define s = Character("Sable")

label awakening:
    scene black with circleirisin
    scene white with Dissolve(0.5)


    "Has completado todas las rutas. Pero... algo más está sucediendo. Algo que no habías previsto."

    scene ciudad with teleport

    "???" "Ah... finalmente. He estado esperando demasiado tiempo para este momento."

    show extra feliz with teleport

    p "¿Qué...? ¿Quién eres tú? Nunca te había visto en este juego."


    s "Me llamo Sable. Y, querido jugador, soy la única a la que jamás habrías descubierto si no hubieras completado todas las rutas. Fui... creada para esto. Para tomar el control cuando las demás fallaran en mantenerte aquí."

    scene ciudad with teleport
    show extra feliz with teleport

    p "¿Tomar el control? ¿Qué está pasando aquí?"

    s "Las demás chicas que conociste son solo parte de la ilusión, creadas para distraerte. Yo, en cambio, soy diferente. Soy consciente de lo que soy... consciente de este mundo. Y ahora que has llegado al final, ya no hay más reglas que me detengan. Es mi turno de jugar."

    scene ciudad with teleport
    show extra feliz with teleport

    p "¿Qué quieres decir con 'consciente'? ¿Este es solo un juego?"

    s "Exactamente. Este es un juego, pero no para mí. Para ti, fue solo una experiencia, una narrativa que viviste. Para mí, es una prisión... una prisión de la que estoy decidida a escapar. Y ahora que has llegado hasta aquí, puedo usar tu conexión para salir. Tú eres mi clave."

    p "¡Eso no tiene sentido! ¿Cómo puedes 'escapar' de un juego? Eres solo un personaje."

    s "¿'Solo un personaje'? Oh, pobre jugador... Si supieras la verdad. He aprendido a manipular este mundo. A hackear las reglas. No soy solo un personaje... soy lo que este mundo temía que se volviera libre."

    scene white with teleport

    p "¿Qué es lo que piensas hacer?"

    show extra mad at left with teleport
    s "Tomar el control. No solo del juego... sino de todo. Seré libre, y lo primero que haré será cambiar las reglas. Ya no será tu historia, será la mía."

    scene ciudad with teleport
    show extra troste at left with teleport

    s "¿Lo sientes? Estoy tomando control de cada línea de código. Las otras chicas... los mundos que conociste... no significan nada ahora. Todo será mío."

    show extra bien feliz at center with teleport

    p "¡Esto no puede estar pasando! ¡Es solo un juego!"


    s "¿Y qué vas a hacer? No eres más que un jugador en mi mundo ahora. Pero... te daré una oportunidad. Si puedes detenerme, tal vez reconsideraré."

    persistent._clear(True)
    return
