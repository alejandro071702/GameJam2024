# define web = Character('Sunny', color = "#BEA665")
label webEvent_Project_start:
     jump webEvent_Project_Event_1


label webEvent_Project_Event_1:     
     $ development = 0
     scene bg_mono_interfaces
     show web feliz

     web "Thanks so much for doing this with me, [name]! I’ve been wanting to create something fun for ages, but, ahh... I keep getting lost in all my ideas!"
     p "(She seems very excited but we are short in time.)"
     
     menu:
          "Let's narrow down the features":
               $ development = development + 1
               jump webEvent_Project_GuideHerBack
          "Your doodles are cute!":
               jump webEvent_Project_EngageHerCreativity

label webEvent_Project_2:
     scene black with circlewipe
     "" "Some time later..."
     scene bg_mono_interfaces with circlewipe

     show web feliz
     web "Look we can add mascots here"
     show web muyfeliz
     web "And we can animate them too!"

     menu:
          "Bring her back to focus":
               $ development = development + 1
               jump webEvent_Project_FocusBack
          "Encourage her creative approach":
               jump webEvent_Project_EncourageHer
     
label webEvent_Project_3:
     scene black with circlewipe
     "" "Some time later..."

     if development < 1:
          "" "The code starts falling behind and you start to notice some bugs cropping up in the development window"

     scene bg_mono_interfaces with circlewipe
     show web feliz

     menu:
          "Suggest correct errors":
               $ development = development + 1
               jump webEvent_Project_CorrectErrors
          "Let her flow freely":
               jump webEvent_Project_FlowFreely

label webEvent_Project_Extra:
     scene black with circlewipe
     "" "As you both try to test the app countless error pop-ups appear"
     scene bg_mono_interfaces with circlewipe
     show web triste
     web "Oh no, I think we got a little too distracted..."
     web "But at least it looks cute! Right? Heheh..."
     web "Do you think people will like it? I don’t want to disappoint anyone."
     menu:
          "Reassure her":
               $ development = development + 1
               jump webEvent_Project_ReassureHer
          "Loaf around":
               jump webEvent_Project_LoafAround

label webEvent_Project_4:
     scene black with circlewipe
     if development < 2:
          "" '(The screen shows the app development phase ending, and a pop-up message appears: "App version: Unstable - Buggy and incomplete.")'
     else:
          "" '(The screen shows the app being successfully tested with minimal bugs, and a pop-up message appears: "App version: Stable - Ready for user testing!")'
     
     if development < 2:
          show web triste
          web "I don't think we have time to correct all the errors."
          web "Everyone will be disapointed."
          web "Sorry [name], could you leave me alone for a moment?."
          scene black with Dissolve(1.0)
          "" "You leave with a heavy atmosphere behind you."
     else:
          show web muyfeliz
          web "We did it! And it even works! Oh my gosh, I’m so happy!"
          web "Thanks so much, [name]. I know I’m not the easiest to work with sometimes, but you really helped me stay on track. Do you think people will like it?"
          show web feliz
          p "I'm sure they'll love it."

     return

label webEvent_Project_GuideHerBack:
     # scene bg_mono_interfaces
     p "Let's narrow down the features. We should focus on the core idea first."
     show web molesto
     pause(1.0)
     web "Hmm… yeah, you’re right. I tend to get carried away."
     show web feliz
     web "Okay! Let's focus on... the core mechanics! We’re doing a to-do list app, right? It needs to be helpful and..."
     show web muyfeliz
     web "Oh! And it should have cute icons!"
     jump webEvent_Project_2
     # return

label webEvent_Project_EngageHerCreativity:
     # scene bg_mono_interfaces
     show web muyfeliz
     web "Ohhh! I like that idea!"
     show web feliz
     web "What if the app had little characters that appear when you finish a task?"
     web "They could cheer you on, like..."
     show web muyfeliz
     web "Yay! You did it!’"
     jump webEvent_Project_2
     # return

label webEvent_Project_FocusBack:
     p "That's a great addition! But let’s keep the code simple for now and add that later."
     if development > 1:
          show web triste
          web "Ahh, I guess I’m doing it again, huh?"
          show web feliz
          web "Okay, okay. Let’s stick to the essentials first."

     web "You know, I’m always worried about being too scattered..."
     web "I’m glad you are here to make me focus more in the development"
     p "Don’t worry about that right now. Let’s just finish this first version!"
     jump webEvent_Project_3

label webEvent_Project_EncourageHer:
     p "I like the mascots. Let’s see how they’d look in the app!"
     show web muyfeliz
     web "Eee, you really think so? That would make the app so cute!"
     jump webEvent_Project_3

label webEvent_Project_CorrectErrors:
     p "Maybe we should handle these bugs first?"
     web "What bugs?"
     "" "You show her the app log with multiple alerts and errors"

     show web triste
     web "What!?"
     web "I didnt notice"

     p "Its okay. We can fix them"
     show web feliz
     web "Yeah, you are right"

     if development < 2:
          jump webEvent_Project_Extra
     else:
          jump webEvent_Project_4

label webEvent_Project_FlowFreely:
     if development < 2:
          p "(We can always clean it up later)"

     if development < 2:
          jump webEvent_Project_Extra
     else:
          jump webEvent_Project_4

label webEvent_Project_ReassureHer:
     p "We can still fix it. There is no need to worry."
     show web feliz
     web "Yeah you are right"

     jump webEvent_Project_4

label webEvent_Project_LoafAround:
     p "It needs more work, but we’re still learning"
     p "Let’s just enjoy the process"
     show web molesto
     web "I'm not sure but i'll trust you"

     jump webEvent_Project_4

