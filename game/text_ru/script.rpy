# Вы можете расположить сценарий своей игры в этом файле.

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    show screen debug()
    call params
    jump morning1_1

    return


label params:
    $uh = 0
    $od = 50
    $zn = 0
    # Определение персонажей игры.
    $time_of_day = "day"
    $nvl_mode = "phone"
    return