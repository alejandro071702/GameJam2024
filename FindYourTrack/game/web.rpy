label webEvent_Project_start:
     jump webEvent_Project_Event_1

label webEvent_Project_Event_1:     
     $ development = 0
     scene bg_mono_interfaces
     show web feliz

     web "¡Muchas gracias por hacer esto conmigo, [name]! Simpre he querido crear algo divertido, pero, ahh... ¡Siempre me pierdo en todas mis ideas!"
     p "(Ella parece muy emocionada, pero estamos cortos de tiempo.)"
     
     menu:
          '"Hay que enfocarnos en las características"':
               $ development = development + 1
               jump webEvent_Project_GuideHerBack
          '"¡Tus dibujos son lindos!"':
               jump webEvent_Project_EngageHerCreativity

label webEvent_Project_2:
     scene black with circlewipe
     # "" "Some time later..."
     scene bg_mono_interfaces with circlewipe

     show web feliz
     web "Mira, podemos agregar mascotas aquí"
     show web muyfeliz
     web "¡Y también podemos animarlas!"

     menu:
          '"Mantengamos el código simple por ahora"':
               $ development = development + 1
               jump webEvent_Project_FocusBack
          '"¡Veamos cómo se verían en la app!"':
               jump webEvent_Project_EncourageHer
     
label webEvent_Project_3:
     scene black with circlewipe
     # "" "Some time later..."

     if development < 1:
          "" "El código comienza a quedarse atrás y empiezas a notar algunos errores que aparecen en la ventana de desarrollo"

     scene bg_mono_interfaces with circlewipe
     show web feliz

     menu:
          '"Deberíamos corregir los errores"':
               $ development = development + 1
               jump webEvent_Project_CorrectErrors
          '"Enfoquemonos en la interfaz"':
               jump webEvent_Project_FlowFreely

label webEvent_Project_Extra:
     scene black with circlewipe
     "" "Al intentar probar la aplicación, aparecen innumerables ventanas emergentes de error"
     scene bg_mono_interfaces with circlewipe
     show web triste
     web "Oh no, creo que nos distraímos un poco..."
     show web feliz
     web "¡Pero al menos se ve lindo! ¿Verdad? Jeje..."
     show web triste
     web "¿Crees que le gustará a la gente? No quiero decepcionar a nadie."
     menu:
          '"Hay que mantener la calma"':
               $ development = development + 1
               jump webEvent_Project_ReassureHer
          '"No le des importancia"':
               jump webEvent_Project_LoafAround

label webEvent_Project_4:
     scene black with circlewipe
     if development < 2:
          "" '(La pantalla muestra el final de la fase de desarrollo de la aplicación, y aparece un mensaje emergente: "Versión de la aplicación: Inestable - Con errores e incompleta.")'
     else:
          "" '(La pantalla muestra la aplicación siendo probada con éxito y con errores mínimos, y aparece un mensaje emergente: "Versión de la aplicación: Estable - Lista para pruebas de usuario.")'
     
     if development < 2:
          show web triste
          web "No creo que tengamos tiempo para corregir todos los errores."
          web "Todos estarán decepcionados."
          web "Lo siento [name], ¿podrías dejarme sola por un momento?"
          scene black with Dissolve(1.0)
          "" "Te vas dejando una atmósfera pesada detrás de ti."
     else:
          show web muyfeliz
          web "¡Lo logramos! ¡Y hasta funciona! ¡Oh Dios mío, estoy tan feliz!"
          web "Muchas gracias, [name]. Sé que a veces no soy la más fácil de trabajar, pero realmente me ayudaste a mantenerme enfocada. ¿Crees que a la gente le gustará?"
          show web feliz
          p "Estoy seguro de que les encantará."

     return

label webEvent_Project_GuideHerBack:
     # scene bg_mono_interfaces
     p "Vamos a reducir las características. Deberíamos enfocarnos primero en la idea principal."
     show web molesto
     pause(1.0)
     web "Hmm... sí, tienes razón. Tiendo a emocionarme demasiado."
     show web feliz
     web "¡De acuerdo! Enfoquémonos en... ¡las mecánicas principales! Estamos haciendo una app de lista de tareas, ¿cierto? Tiene que ser útil y..."
     show web muyfeliz
     web "¡Oh! ¡Y debería tener íconos muy lindos!"
     jump webEvent_Project_2
     # return

label webEvent_Project_EngageHerCreativity:
     # scene bg_mono_interfaces
     show web muyfeliz
     web "¡Ohhh! ¡Me gusta esa idea!"
     show web feliz
     web "¿Y si la app tuviera pequeños personajes que aparecieran cuando terminas una tarea?"
     web "Te podrían animar, como..."
     show web muyfeliz
     web "¡Yay! ¡Lo lograste!"
     jump webEvent_Project_2
     # return

label webEvent_Project_FocusBack:
     p "Siempre podemos agregar mas cosas después."
     if development > 1:
          show web triste
          web "Ahh, supongo que lo estoy haciendo de nuevo, ¿eh?"
          show web feliz
          web "Está bien, está bien. Enfoquémonos en lo esencial primero."

     web "Sabes, siempre me preocupa estar demasiado dispersa..."
     web "Me alegra que estés aquí para ayudarme a concentrarme más en el desarrollo."
     p "No te preocupes por eso ahora. ¡Vamos a terminar esta primera versión!"
     jump webEvent_Project_3

label webEvent_Project_EncourageHer:
     show web muyfeliz
     web "¡Eh, ¿de verdad crees eso? Eso haría que la app fuera tan linda!"
     jump webEvent_Project_3

label webEvent_Project_CorrectErrors:
     
     web "¿Qué errores?"
     "" "Le muestras el registro de la aplicación con múltiples alertas y errores."

     show web triste
     web "¡¿Qué?!"
     web "No me di cuenta."

     p "Está bien. Podemos arreglarlos."
     show web feliz
     web "Sí, tienes razón."

     if development < 2:
          jump webEvent_Project_Extra
     else:
          jump webEvent_Project_4

label webEvent_Project_FlowFreely:
     if development < 2:
          p "(Siempre podemos limpiar todo más tarde)"

     if development < 2:
          jump webEvent_Project_Extra
     else:
          jump webEvent_Project_4

label webEvent_Project_ReassureHer:
     p "Podemos arreglarlo. No hay necesidad de preocuparse."
     show web feliz
     web "Sí, tienes razón."

     jump webEvent_Project_4

label webEvent_Project_LoafAround:
     p "Necesita más trabajo, pero aún estamos aprendiendo."
     p "Disfrutemos del proceso."
     show web molesto
     web "No estoy seguro, pero confiaré en ti."

     jump webEvent_Project_4

