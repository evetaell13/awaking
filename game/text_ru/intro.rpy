

label intro1:
    scene street_panorama with dissolve:
        xalign 0.0
    show street_panorama at panorama
    mistik "Улицы Васильевского острова помнят многое..."
    mistik "Порой они живут своей собственной, таинственной жизнью, нередко вмешиваясь в судьбы людей и заставляя тех следовать своей воле."
    mistik "Жители знают, что после развода мостов лучше не выходить из дома."
    mistik "А гости стараются сбежать пораньше, ощущая спиной чей-то чуждый взгляд из черной глади Невы."
    mistik "Вот только не всем удается просто так уйти..."

    jump intro2


label intro2:
    # with fade_all
    scene most with fade_all
    nar "Девушка бежала под проливным дождем, зная, что не успеет."
    scene most2 with fade_all
    alina "Нет...нет...нет..! "
    scene most with fade_all
    nar "Девушка рычит..."
    scene most2 with fade_all
    nar "Девушка ползет..."
    scene most with fade_all
    nar "Девушка рычит..."
    return