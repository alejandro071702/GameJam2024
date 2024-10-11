define f = 0
label cloud1:
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
    p "¡Espera, no estoy entendiendo!"
    hide cloud feliz
    "" "..."
    scene bg_mono_pasillo
    p "Al menos estoy seguro de que puedo pedirle ayuda..."
    jump iot1
label iot1:
    p "Hora de mi siguiente clase"
    scene bg_mono_micro
    show iot feliz with sl_easein
    iot "Oye, vas en mi equipo para la práctica. Ponte a programar esto."
    p "(Chipi-chan. Suele pedirme que haga cosas para las prácticas, y yo sólo obedezco sin importar qué me pida.)"
    p "(Ambos sabemos que hubiera reprobado sin oportunidad de recuperarme desde el principio si no fuera porque me trae de acá para allá para las prácticas y añade mi nombre en los reportes)."
    p "(Gracias a ella es que esta es la única materia que no voy reprobando.)"
    scene bg_mono_micro with circlewipe
    iot "Gracias, limpia la mesa antes de irte."
    hide iot feliz
    p "..."
    scene bg_mono_pasillo with circlewipe
    jump webAndGeo1
label webAndGeo1:
    scene bg_mono_pasillo with circlewipe
    show web bien feliz at left with sr_easein
    web "¡Hola, [name]!"
    show alpha_filter behind web
    p "(Sunny. Es así de amigable con todos los que se encuentra. Al menos eso es lo que he visto)"
    hide alpha_filter
    web "¿Hiciste el ejercicio de ayer? Yo no estoy seguro de qué tan bien me quedó. ¿Puedo compararlo con el tuyo?"
    p "No, olvidé terminarlo."
    web "Cómo crees. ¿Qué vas a hacer, entonces?"
    p "No sé, copiarlo de algún lado."
    geo "¡No, no copies su tarea!"
    show geo molesto at right with sl_easein
    geo "Si haces eso, no vas a aprender nada. Mejor intenta hacerla después de decirle al profesor."
    show alpha_filter behind geo
    show web behind alpha_filter
    p "(Mappu. Demasiado molesta para su propio bien)."
    p "(Estudiamos en la misma escuela desde la secundaria y los únicos recuerdos que tengo de ella son cuando se quejaba con los profesores.)"
    hide alpha_filter
    geo "Te puedo ayudar a hacer la tarea. Sólo tienes que pedírmelo la próxima vez."
    p "(Por más insoportable que pueda ser, no puedo rechazar su oferta. Necesito pasar esta materia)."
    "Profesor" "Así tiene que quedar su proyecto. Es en equipos, escojan bien con quién se juntan para evitar pleitos."
    p "(Me lleva. También necesito recuperarme en esta materia (vaya sorpresa), debo elegir bien, y creo que sólo tengo dos opciones)."
    p "(Mappu. El trabajo definitivamente será más tedioso, pero al menos juntarme con ella asegura que saldrá)."
    p "(Trabajar con Sunny definitivamente será más relajado, aunque no sé si pueda ayudarme a pasar la materia tan bien como con Mappu)."
    menu:
        '"Mappu"':
            geo "¿Quieres ir en MI equipo? Nunca te he visto trabajar bien, voy a decirle al profesor que te consiga otra pareja."
            p "Ya no hay más gente libre. No nos queda de otra que trabajar juntos."
            geo "..."
            geo "¡Bien, pero tendrás que trabajar como yo te diga!"
            p "Es eso o reprobar."
            geo "Más te vale..." 
            $ f = 1
        '"Sunny"':
            web "¿Quieres ir en mi equipo? ¡Claro! Pero debes prometerme que ayudarás y no me dejarás todo el trabajo a mí."
            p "Claro, necesito practicar para entender todo lo que no he aprendido en el semestre."
            web "Genial, podemos repasar luego si quieres."
            $ f = 0
    scene bg_mono_pasillo with circlewipe
    p "(Tengo mucho trabajo que hacer si quiero continuar la carrera. Sólo espero que una de las personas que acabo de conocer me ayude a aprobar)."
    p "Espero que medio semestre sea suficiente..."
    jump nextday
label nextday:
    scene bg_dormitorio with circlewipe
    p "Ahora, creo que sería prudente decidir en qué enfocarme. No podría dar el mismo esfuerzo en tres materias distintas y mucho menos con cuatro personas distintas."
    p "Mejor organizo mis ideas y me propongo en dar la mayor parte de mi energía a una persona."
    p "Todas mis materias están en riesago, pero mejor salgo sobresaliente en una, por si acaso."
    $ x = 0
    if persistent.geoF == True and persistent.webF == True and persistent.iotF == True and persistent.cloudF == True:
        menu:
            'T̷̢̛̪͔̘͓̆̎̿͒̽̍͛̎̈͊͆̍̊̕ͅH̴̛̹̩̻̭͓͙͍͙͊̌̈̽̂́̋̐͛̂͐͜e̷͚̊͐̾͑̓͛̓́͑͗̀̅̽ͅr̶̟͚͖̣̬͓͕͕̻̗̜̣̬̒̍͛̐̂̇̽̽̈́̒̇͑̒e̷̻͔̩̱̮̻̪͍̰̓ ̸̡̢̫̰͍͈̞̪̣̞̍̊͠i̴̖̘̗̥̫͆̃̏̍̓̉̃̎̕S̴̮̻͖̣̱̹̖͋̈́͒̓͗͋̀͒̓ͅ ̸̧̡̲̱̩̰̙͇̗̫͍̬͉̬̮̔̓̐̕͝o̶̥͈̳̺̺̱̙͇͈͕̗̯̦̽̌͒͗̽͂̔̕͝n̷̢̰̞͔̭͍̋͆̂͋͂̏̓̂̐̔̀͆̂͘ͅL̵̩̦̦̹̼̺̩̗͉͒̃ỳ̵̡̜̟͍̻̮͖͗͠ ̶̭̫̯͈̘̣͕̦̥͊̀̀̊̏͐͗̈́̈́̀̈͜͝͝O̷̹͓͐̾̇͌̈́̒͌͂n̷̺͎̩͕̰̝̥̙͈̊͑̇̊͗̅̓͂̈e̷͔̣͈̣͙͕̮͖̫͚̾̊̇̊͒̽̆̍́̍̀̎̕͜':
                return
    elif f == 1:
        menu:
            '"Debería intentar estudiar más con Claudia"':
                p "Claudia es muy lista. Probablemente me convenga pedirle estudiar conmigo."
                $ x = 0
            '"Podría avanzar el proyecto con Mappu"':
                p "Me conviene adelantar el trabajo con ella. Sería menos tiempo que pasaré con ella."
                $ x = 1
            '"Ir con Chipi-chan suena a una buena idea"':
                p "Es bastante lista, algo se me debería pegar."
                $ x = 2
            '"Tal vez Sunny sea la mejor opción"':
                p "Es la más amigable de mis opciones, y estudiar con ella probablemente sea menos pesado."
                $ x = 3
            '"Mejor hago todo solo. Cómo no voy a poder"':
                $ x = 4
    else:
        menu:
            '"Debería intentar estudiar más con Claudia"':
                p "Claudia es muy lista. Probablemente me convenga pedirle estudiar conmigo."
                $ x = 0
            '"Podría avanzar el proyecto con Sunny"':
                p "Es la más amigable de mis opciones, y estudiar con ella probablemente sea menos pesado."
                $ x = 3
            '"Ir con Chipi-chan suena a una buena idea"':
                p "Es bastante lista, algo se me debería pegar."
                $ x = 2
            '"Tal vez Mappu sea la mejor opción"':
                p "Por más molesta que sea, sabe mucho. Y de verdad necesito aprender."
                $ x = 1
            '"Mejor hago todo solo. Cómo no voy a poder"':
                $ x = 4
    scene bg_dormitorio with circlewipe
    if x == 0:
        jump cloud_dia2
    elif x == 1: 
        jump geoDay2
    elif x == 2:
        jump iotDay2
    elif x == 3:
        jump webDay2
    else:
        jump badEnding