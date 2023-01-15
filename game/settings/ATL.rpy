init:

    # Анимация панорамы
    transform panorama:
        xalign 0.0
        linear 10.0 xalign 1.0
        repeat 1

        # pause 0.1
        # # xpan 0
        # linear 20.0 xpan 0
        # repeat 1

    # Анимация вспышки
    define fade_all = Fade(0.2, 0.0, 0.8, color="#FFFFFF")

init python:
    memory_1 = ImageDissolve("images/atl/diagonal1.jpg", 2.0, 80, reverse=False)
    memory_2 = ImageDissolve("images/atl/diagonal1.jpg", 2.0, 100, reverse=True)