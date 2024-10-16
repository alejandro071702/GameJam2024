label webDay2:
    show web feliz
    p "(Veo a todos muy preocupados, ¿olvidé hacer algún proyecto?)"
    p "(¡No puede ser! Olvidé el examen, no he estudiado nada y no creo alcanzar a ver en una noche, menos 5 minutos antes)"
    web "¡Hola, user! ¿Emocionado por el examen de mañana? Llevo desvelándome toda la semana, estoy segura de que me irá bien."
    p "(Qué animada, ¿quién se alegra por un examen?) Eh... en realidad no. No he estudiado nada... y no entiendo nada."
    web "Pero no es tan difícil. Si pudiste hacer los ejercicios que encargó el profesor, no creo que tengas problema."
    p "¿Crees qué puedas explicarme más tarde? Si tienes tiempo libre."
    web "Tengo mi agenda muy apretada, pero ¡va! Te veo más tarde."
    "" "..."
    p "(Llevo esperando a Sunny, no la veo por ningún lado. Espero que sí venga.)"
    web "¡Hey! Perdón por la tardanza, tenía un compromiso."
    p "Está bien, no te preocupes."
    " " "Estudianding..."
    p "... Ah, muchas gracias, creo que ya entiendo mejor los temas. Se nota que te gusta mucho esta materia."
    web "¡Sí! Siempre me ha gustado mucho el diseño, dibujar y el frontend, además quiero enfocarme en el Área de Énfasis de Desarrollo Web y Multiplataforma"
    p "¿En serio? Yo aún no decido que área elegir... pero dime, ¿por qué te interesa esa en especifico?"
    web "El desarrollo web y multiplataforma es interesante por su accesibilidad global, versatilidad al funcionar en múltiples dispositivos, constante evolución tecnológica, alta demanda laboral, y por permitir creatividad en la creación de experiencias interactivas."
    p "Genial... Suena interesante, no había puesto tanta atención a lo que conlleva el área."
    web "Podría hablar todo el día, ¿quieres que siga?"
    p "Sí, por favor."
    web "Bueno, ahondando en cada característica que te mencioné, es interesante porque las aplicaciones web son accesibles desde cualquier dispositivo con conexión a Internet, lo que permite a los desarrolladores llegar a un público más amplio. De igual manera, el desarrollo multiplataforma permite crear aplicaciones que funcionen en diferentes sistemas operativos como Windows, macOS, Android e iOS con un solo código base, lo que ahorra tiempo y recursos. También, la tecnología web está en constante evolución, lo que brinda oportunidades para aprender y aplicar nuevas herramientas y frameworks, como React, Angular o Vue.js. Y una gran ventaja es que hay una alta demanda de desarrolladores web y multiplataforma en el mercado laboral, lo que significa mejores oportunidades de empleo y crecimiento profesional. Y el principal motivo por el cual me gusta es porque el desarrollo web permite la creación de experiencias interactivas y visuales, lo que estimula la creatividad y la innovación."
    p "(Ah mi mente, demasiada información para mí)"
    p "Así cómo lo explicaste sí suena bien chevere."
    web "¿Verdad que sí?, ¿qué fue lo que te llamó la atención?"
    menu:
        '"Me llamó la atención que las aplicaciones sean accesibles desde cualquier dispositivo con conexión a Internet."':
            web "A mí también."
        '"Que será fácil conseguir trabajo."':
            web "Sí, muchos lo eligen por eso."
        '"El dorado de tus ojos."':
            web "Estamos hablando del desarrollo web."
            scene bg_dormitorio with circlewipe
            jump badEnding
    web "Aunque, tiene sus desventajas, si no tienes internet no será funcional."
    p "(No me interesaba para nada esa área, pero ella lo hace ver interesante)"
    "" "..."
    p "(Nos quedamos un par de horas hablando, fue muy intrigante conocer más acerca del área de desarrollo web. Tampoco había notado lo linda que se ve hablando de lo que la apasiona)"

    jump webDay3
