label badEnding:
    scene bg_dormitorio with circlewipe
    define na = Character(None, what_xalign=0.5, what_color="#E6E6E6", who_outlines=[ (1, "#000000")], what_text_align=0.5,  text_xpos=0.5,  text_ypos=0.5, what_minheight=200, kind=nvl)
    p "No debí elegir estudiar solo. No supe ni por dónde empezar."
    na "[name] se murió solo y triste sin poder titularse."
    na "Aprende de sus errores y échale ganas a la vida"
    nvl clear
    na "Perdistes carnal"
    $ persistent.iotF = True
    $ renpy.save_persistent()
