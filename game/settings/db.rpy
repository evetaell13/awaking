init:
    image side alina_ava  = Image("images/ava/alina_ava.png")
    # image side babka  = Image("images/ava/alina_ava.png")
    # image side alina_ava  = Image("images/ava/alina_ava.png")
    # image side alina_ava  = Image("images/ava/alina_ava.png")

    define nar = Character(None, what_xpos = 50, what_line_leading = 12, what_ypos = 100, what_xsize = 1870)
    # define nar = Character("", what_line_leading = 12, kind=nvl)
    define alina = Character("", image="alina_ava", what_line_leading = 12, what_ypos = 10, what_xsize = 1370)
    define kate = Character("", image="alina_ava", kind=alina)
    define artem = Character("", image="alina_ava", kind=alina)
    define ag = Character("", image="alina_ava", kind=alina)
    define dan = Character("", image="alina_ava", kind=alina)
    define psyh = Character("", image="alina_ava", kind=alina)
    define mistik = Character("", image="alina_ava", kind=alina)

init python:

    nar_w = 0

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
