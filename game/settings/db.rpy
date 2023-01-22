init:
    image side alina_ava  = Image("images/ava/alina_ava.png")
    image side babka_ava  = Image("images/ava/babka_ava.png")
    image side kate_ava  = Image("images/ava/kate_ava.png")
    image side artem_ava  = Image("images/ava/artem_ava.png")
    image side dan_ava  = Image("images/ava/dan_ava.png")
    image side prepod_ava  = Image("images/ava/prepod_ava.png")

    define nar = Character(None, window_background=Image("gui/textbox_nar.png", xalign=0.5, yalign=1.0), what_xpos = 180, what_line_leading = 12, what_ypos = 10, what_xsize = 1580)
    define alina = Character("", image="alina_ava", window_background=Image("gui/textbox.png", xalign=0.5, yalign=1.0), what_line_leading = 12, what_ypos = 10, what_xsize = 1370)
    define kate = Character("", image="kate_ava", kind=alina)
    define artem = Character("", image="artem_ava", kind=alina)
    define ag = Character("", image="babka_ava", kind=alina)
    define dan = Character("", image="dan_av", kind=alina)
    define psyh = Character("", image="alina_ava", kind=alina)
    define mistik = Character("", image="alina_ava", kind=alina)
    define bufet_women = Character("", image="alina_ava", kind=alina)
    define prepod = Character("", image="prepod_ava", kind=alina)
    define alina_m = Character("", image="alina_ava", kind=alina, what_prefix="\"", what_suffix="\"")

init python:

    skills_tb = {

    }

    inv_tb = {

    }

    

    # phone
    a_nvl = Character("Алина", kind=nvl, image="", callback=Phone_SendSound)
    k_nvl = Character("Катя", kind=nvl, callback=Phone_ReceiveSound)

    # config.adv_nvl_transition = None
    # config.nvl_adv_transition = Dissolve(0.3)

init:
    image room_gg = ConditionSwitch(
        "time_of_day == 'day'", "bg/room_gg_day.jpg",
        "time_of_day == 'night'","bg/room_gg_night.jpg",
    )
