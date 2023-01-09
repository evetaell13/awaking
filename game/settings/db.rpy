init python:

    skills_tb = {

    }

    inv_tb = {

    }

    nar = Character(None, what_xpos = 30, what_line_leading = 12, what_ypos = 30, what_xsize = 1890, image="", what_layout='subtitle')
    alina = Character('Алина', color="#c8ffc8")
    kate = Character('Катя', color="#c8ffc8")
    artem = Character(_("boy"), dynamic=True, color="#c8ffc8")
    ag = Character(_("babka"), dynamic=True, color="#c8ffc8")
    dan = Character(_("barmen"), image="", dynamic=True, color="#c8ffc8")
    psyh = Character(_("psyh_name"), color="#c8ffc8", dynamic=True)
    mistik = Character('Женщина в сером', color="#c8ffc8")

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
