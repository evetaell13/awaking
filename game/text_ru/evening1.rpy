label evening1_1:
    nar "Из промозглого вечера через пропахшую щами парадную я зашла в квартиру. В ботинках хлюпал дождь, влажный холодный ветер выстудил всю душу."
    ag "Алиночка, ты похоже совсем продрогла."
    ag "Пойдем налью тебе кофе с анисом и лимоном, сразу станет легче."
    alina "Кофе - это то что мне сейчас нужно."
    nar "" #todo
    ag "Пей осторожно, деточка."
    ag "Ты знаешь, что первым кофе начал готовить йеменский шейх Абд-аль-Кадир. Он был алхимиком. Изучал разные травы и плоды на пути познания истины. Расширял границы сознания - так теперь сказали бы... Кхе-кхе."
    ag "\"Никто не может понять истины, пока не вкусит кофейного пенного блаженства\", - говорил Кадир."
    ag "В этом городе без кофе просто нельзя прожить... Такое уж тут место."
    alina "Какое такое?"
    ag "Этот город не такой, как другие, Алина. Это городь-тень, город-топь, выстроенный на болоте, в месте где никогда прежде не жили люди."
    #todo дописать действия и реакции
    ag "Люди не жили, но в водах Невы обитало нечто или некто..."
    ag "Говорят, Питер построен на крови тысяч замученных рабочих. А я вот думаю, не была ли эта кровь -- жертвой тому, что обитало в этих болотах, платой за право построить здесь город вопреки законам мира и здравого смысла."
    ag "Есть легенда что мосты разводят вовсе не для прохода короблей, а чтобы по ночам не выпускать в город то, что обитает на Васильевском острове. Что обитало там задолго до того, как появились мосты и город."
    jump evening_tale

label evening_tale:
    menu:
        ag "Я знаю, теперь ты это тоже чувствуешь."
        "Отмахнуться и пойти спать":
            alina "Мне пожалуй пора спать."
            alina "Спасибо за кофе, Аврора Говардовна. Очень вкусно."
        "Узнать подробности":
            $uh = uh + 10
            alina "Откуда вы знаете, что я чувствую?"
            ag "Потому что ты не одна так чувствуешь. Это поселилось в тебе."
            ag "Доктор говорит, когда постоянно мерзнешь даже в теплой квартире, в голове туман и кажется что погружаешься в топь, нужно пить таблетки."
            ag "Но я предпочитаю кофе с коньяком. И затянуться сигареткой."
            nar "Мне стало не по себе. Как будто из окон на меня..." #todo
            alina "Мне пожалуй хватит кофе на сегодня. А вам - коньяка."
            alina "Спасибо Аврора Говардовна, я пойду к себе."
        "Не поверить":
            $uh = uh + 5
            alina "Эта же просто городская легенда, да? Зачем вы меня пугаете?"
            ag "Не хочешь слушать сумасшедшую старуху? Правильно делаешь, деточка. Никого не слушай, особенно голоса в голове."
            ag "Их вообще никогда не надо слушать и не надо делать, что они говорят."
            alina "Спокойной ночи, Аврора Говордовна. Спасибо за кофе."
    alina "\"Безумие какое-то. Реальность словно просачивается сквозь пальцы. Бабка ещё эта со своим бредом. Это всё от недосыпа.\""
    alina "\"Вот высплюсь нормально и завтра всё будет нормально, без этого горячечного бреда.\""
    jump dream_1

label dream_1:
    "Тихий голос: От себя не убежишь."
    "Тихий голос: От себя не спрячешься."
    "Тихий голос: Я - это ты."
    "Девушка из сна: Если ты - это я, то я знаю как от тебя избавиться."
    jump morning2_1