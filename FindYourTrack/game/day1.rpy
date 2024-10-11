
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
    p "(iotGirl. Suele pedirme que haga cosas para las prácticas, y yo sólo obedezco sin importar qué me pida.)"
    p "(Ambos sabemos que hubiera reprobado sin oportunidad de recuperarme desde el principio si no fuera porque me trae de acá para allá para las prácticas y añade mi nombre en los reportes)."
    p "(Gracias a ella es que esta es la única materia que no voy reprobando.)"
    scene bg_mono_micro with circlewipe
    iot "Gracias, limpia la mesa antes de irte."
    hide iot feliz
    p "..."
    scene bg_mono_pasillo with circlewipe
    jump webAndGeo1
label webAndGeo1:
    scene bg_mono_pasillo with circle
    show web bien feliz at left with sr_easein
    web "¡Hola, {name}!"
    show alpha_filter behind web
    p "(webGirl. Es así de amigable con todos los que se encuentra. Al menos eso es lo que he visto)"
    web "¿Hiciste el ejercicio de ayer? Yo no estoy seguro de qué tan bien me quedó. ¿Puedo compararlo con el tuyo?"
    p "No, olvidé terminarlo."
    web "Cómo crees. ¿Qué vas a hacer, entonces?"
    p "No sé, copiarlo de algún lado."
    geo "¡No, no copies su tarea!"
    show geo molesto at right with sl_easein
    geo "Si haces eso, no vas a aprender nada. Mejor intenta hacerla después de decirle al profesor."
    show alpha_filter behind geo
    show web behind alpha_filter
    p "(geoGirl. Demasiado molesta para su propio bien)."
    p "(Estudiamos en la misma escuela desde la secundaria y los únicos recuerdos que tengo de ella son cuando se quejaba con los profesores.)"
    geo "Te puedo ayudar a hacer la tarea. Sólo tienes que pedírmelo la próxima vez."
    p "(Por más insoportable que pueda ser, no puedo rechazar su oferta. Necesito pasar esta materia)."
    "Profesor" "Así tiene que quedar su proyecto. Es en equipos, escojan bien con quién se juntan para evitar pleitos."
    p "(Me lleva. También necesito recuperarme en esta materia (vaya sorpresa), debo elegir bien, y creo que sólo tengo dos opciones)."
    p "(geoGirl. El trabajo definitivamente será más tedioso, pero al menos juntarme con ella asegura que saldrá)."
    p "(webGirl. Definitivamente será más relajado, aunque no sé si pueda ayudarme a pasar la materia tan bien como con geoGirl)."
    menu:
        'Mappu':
            jump geoChosen 
        'Sunny':
            jump webChosen
label geoChosen:
    geo "¿Quieres ir en MI equipo? Nunca te he visto trabajar bien, voy a decirle al profesor que te consiga otra pareja."
    p "Ya no hay más gente libre. No nos queda de otra que trabajar juntos."
    geo "..."
    geo "¡Bien, pero tendrás que trabajar como yo te diga!"
    p "Es eso o reprobar."
    geo "Más te vale..."
    jump continuation
label webChosen:
    web "¿Quieres ir en mi equipo? ¡Claro! Pero debes prometerme que ayudarás y no me dejarás todo el trabajo a mí."
    p "Claro, necesito practicar para entender todo lo que no he aprendido en el semestre."
    web "Genial, podemos repasar luego si quieres."
    jump continuation
label continuation:
    scene bg_mono_pasillo with circlewipe
    

