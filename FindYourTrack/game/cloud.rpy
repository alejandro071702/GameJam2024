#Capítulo 5: Explorando los Principios del Cómputo en la Nube
#[Player y Yoru están sentados juntos, revisando un libro sobre redes y la nube.]
label cloudtest:
    scene bg_biblioteca
    show cloud bien feliz
    p "Aún no entiendo del todo… ¿Qué hace que la nube sea tan diferente del cómputo tradicional?"

    cloud 'El cómputo en la nube se basa en algunos principios clave: escalabilidad, elasticidad, y pago por uso. En lugar de comprar y mantener tus propios servidores, puedes usar los recursos que necesitas desde cualquier lugar y pagas solo por lo que usas.'
    p '¿Es como alquilar en lugar de comprar?'
    show cloud feliz
    cloud 'Exactamente. Es flexible y permite que las empresas crezcan sin tener que invertir en infraestructura física. Además, la nube distribuye los recursos en múltiples ubicaciones, lo que significa que puedes acceder a ellos desde casi cualquier parte del mundo.'
    p 'Interesante… nunca lo había visto como algo tan versátil.'

label cloud_dia2:
    scene bg_mono_salon
    show cloud bien feliz

    p '(Hemos estado hablando de redes y la nube durante un largo tiempo, pero nunca le he preguntado a Cloud por qué eligió esta área. Parece que realmente le apasiona, y tal vez podría aprender algo más profundo de ella si simplemente le pregunto.)'

    p 'Oye, Cloud… ¿puedo preguntarte algo?'

    cloud '(mirando su taza de café, pero atenta)'
    cloud '¿Qué pasa?'

    p '¿Por qué elegiste estudiar esto? Quiero decir, redes, la nube… ¿qué fue lo que te atrajo?'

    cloud '(haciendo una pausa, pensativa)'
    cloud 'Interesante pregunta. No muchos se detienen a preguntar por qué hacemos lo que hacemos.'

    p '(sonriendo levemente)'
    p 'Bueno, siento curiosidad. Te veo siempre tan concentrada, como si esto realmente te importara.'

    cloud '(mirando hacia la ventana, con un tono más suave)'
    cloud 'Elegí esta área de énfasis porque me intrigó cómo la arquitectura en la nube y los servicios en la nube son esenciales para todo lo que implica el cómputo en la nube. Estos dos elementos… son como los pilares que sostienen todo el sistema. Sin ellos, nada funcionaría como lo hace.'

    p '¿La arquitectura en la nube? ¿Como la estructura de todo?'

    cloud '(asintiendo lentamente)'
    cloud 'Exacto. Piensa en la arquitectura en la nube como los cimientos de un edificio, pero en lugar de ladrillos y cemento, usamos servidores, almacenamiento y redes distribuidas globalmente. Es lo que permite que los recursos sean flexibles, escalables, y estén siempre disponibles para los usuarios sin importar dónde estén.'

    show cloud feliz

    p '(interesado)'
    p 'Entonces, ¿todo se basa en eso? ¿Cómo organizas esos recursos?'

    cloud '(con una leve sonrisa)'
    cloud'“Exactamente. La arquitectura define cómo se organizan y gestionan los recursos. Es fascinante porque, aunque parezca que la nube es algo intangible, en realidad es todo un conjunto de componentes físicos y virtuales funcionando en armonía. La organización eficiente de esos recursos es lo que garantiza que cuando alguien necesita más capacidad, la obtenga en el momento preciso. O si el sistema falla en alguna parte, todo se redirige automáticamente sin que el usuario lo note.”'

    p '(pensativo)'
    p 'Entonces, lo que haces con la arquitectura tiene un impacto directo en la experiencia del usuario.'

    cloud '(mirándote con seriedad)'
    cloud 'Exactamente. Cada decisión que tomas en cuanto a la organización de la infraestructura afecta la capacidad de la nube para ser ágil, eficiente y, lo más importante, confiable.'

    p '¿Y los servicios en la nube? ¿Cómo encajan ahí?'

    cloud 'Bueno, los servicios en la nube son como las piezas de un rompecabezas que completan la imagen. Si la arquitectura es la estructura básica, los servicios son los componentes que los usuarios realmente ven y utilizan. Servicios como IaaS (Infraestructura como Servicio), PaaS (Plataforma como Servicio) y SaaS (Software como Servicio) proporcionan diferentes niveles de control y flexibilidad según lo que los usuarios necesiten.'

    p '(curioso)'
    p '¿Qué es lo que te parece tan interesante de eso?'

    cloud '(mirando hacia ti, más abierta)'
    cloud 'Lo que me atrajo es cómo todo esto es adaptable y evolutivo. No es estático, cambia constantemente según las necesidades. Los servicios en la nube pueden crecer con las demandas del mercado. Las empresas no tienen que comprar servidores físicos o preocuparse por límites de almacenamiento; pueden simplemente ajustar lo que necesitan en tiempo real.'

    show cloud bien feliz

    p '(sonriendo)'
    p 'Es como tener un sistema que crece contigo.'

    cloud '(sonriendo levemente)'
    cloud 'Exacto. Esa flexibilidad es lo que más me fascina. Ver cómo los recursos pueden escalar sin esfuerzo es algo que me hace admirar esta tecnología. El mundo digital se mueve tan rápido que si no tienes una infraestructura flexible, te quedas atrás. Y los servicios en la nube son los que hacen posible todo esto, permitiendo que los usuarios se concentren en lo que realmente importa sin tener que preocuparse por lo que está debajo.'

    p '(pensativo)'
    p 'Ahora entiendo mejor por qué te apasiona tanto. Es como construir un mundo invisible que lo sostiene todo.'

    cloud '(mirándote con una expresión suave)'
    cloud 'Es una forma de verlo. Y cuando entiendes cómo funciona desde dentro, es como ver el mundo desde una nueva perspectiva. Me gusta pensar que, de alguna manera, soy parte de esa evolución.'

    p '(sonriendo)'
    p 'Es inspirador. Tal vez haya algo en este mundo de la nube para mí después de todo.'

    show cloud feliz

    cloud 'Tienes alguna duda en algo mas?'

    menu:
        '"¿Cómo administras una red tan grande? "':
            cloud "La administración de redes en la nube implica monitorear el tráfico, asegurarse de que todos los dispositivos estén conectados correctamente y que no haya interrupciones. Existen herramientas específicas para esto, como los sistemas de monitoreo de redes, que te alertan cuando algo falla. Además, tienes que configurar firewalls y reglas de acceso para asegurarte de que solo el tráfico autorizado pase a través de la red."
        '"No ninguna duda!"':
            cloud "bueno, tu te lo pierdes"
        '"Me gusta el azul de tu cabello"':
            web "Gracias!, pero no te distraigas"

    web "Espero no se te olvide lo que platicamos el dia de hoy , nos vemos luego!"


    #Capítulo 10: Modelado y Simulación de Redes
    #scene Laboratorio de simulación de redes
    p '¿Qué es lo que se hace en este laboratorio? Parece diferente a los otros.'
    show cloud bien feliz
    cloud 'Este es el laboratorio de simulación de redes. Aquí modelamos redes complejas para entender su comportamiento antes de implementarlas en la realidad. Usamos software de simulación para ver cómo funcionarán las redes bajo diferentes condiciones, como tráfico alto o fallos en los routers.'

    p '¿Entonces puedes probar todo antes de lanzarlo al mundo real?'

    cloud 'Exacto. Es como tener una versión digital de tu red donde puedes hacer experimentos sin afectar el sistema real. Puedes ver cómo un cambio en la configuración impacta el tráfico de datos, o qué pasa si uno de los enlaces se cae. Es esencial para grandes proyectos de redes en la nube, donde cualquier error puede costar mucho tiempo y dinero.'

    p 'Es como un simulador de vuelo, pero para redes.'

    cloud 'Algo así. Aquí puedes cometer errores y aprender de ellos sin consecuencias graves.'
 