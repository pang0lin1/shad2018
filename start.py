# -*- coding: utf-8 -*-

filename = 'Log'
watch_tv_online = ["телевидение онлайн", "телевидение онлайн бесплатно", "телевидение онлайн смотреть",
                   "телевидение онлайн смотреть бесплатно", "телевидение онлайн прямая",
                   "телевидение онлайн бесплатно без", "телевидения онлайн без регистрация",
                   "смотреть телевидения без онлайна", "телевидение смотреть онлайн бесплатно без",
                   "смотреть телевидение онлайн без регистрации", "телевидения онлайн без регистрация",
                   "смотреть телевидение онлайн без регистрации", "телевидение онлайн бесплатно и без регистрации",
                   "смотреть телевидение онлайн бесплатно и без регистрации",
                   "тв телевидение бесплатно без регистрации онлайн", "телевидение онлайн бесплатно",
                   "телевидение онлайн смотреть бесплатно", "телевидение онлайн бесплатно прямой",
                   "телевидение онлайн эфир бесплатно", "телевидение онлайн бесплатно прямой эфир",
                   "телевидение онлайн смотреть", "телевидение онлайн смотреть бесплатно",
                   "телевидение онлайн смотреть тв", "телевидение онлайн смотреть тв бесплатно",
                   "смотреть телевидения без онлайна", "телевидение онлайн прямая", "телевидение онлайн прямой эфир",
                   "телевидение онлайн бесплатно прямой", "телевидение онлайн бесплатно прямой эфир",
                   "1канал бесплатно онлайн телевидение прямой", "онлайн телевидение эфир",
                   "телевидение онлайн прямой эфир", "телевидение онлайн эфир бесплатно",
                   "телевидение онлайн бесплатно прямой эфир", "1канал бесплатно онлайн телевидение прямой эфир",
                   "тв телевидение онлайн", "телевидение онлайн смотреть тв", "тв онлайн телевидение бесплатно",
                   "телевидение онлайн смотреть тв бесплатно", "тв телевидение бесплатно без регистрации онлайн",
                   "онлайн телевидение все каналы", "каналы телевидения смотреть онлайн",
                   "телевидение онлайн бесплатно все каналы", "онлайн телевидение все каналы смотреть бесплатно",
                   "тв каналы онлайн телевидение", "телевидение онлайн 1 1", "телевидение онлайн 1 1",
                   "телевидение онлайн 1 канал", "телевидение онлайн бесплатно 1 1", "телевидение онлайн бесплатно 1 1",
                   "1канал телевидение онлайн", "1канал бесплатно онлайн телевидение",
                   "1канал бесплатно онлайн телевидение прямой", "1канал бесплатно онлайн телевидение прямой эфир",
                   "1канал бесплатно онлайн телевидение прямой эфир hd"]
watch_tv_program = ["программа на сегодня все каналы", "программа передач на сегодня все каналы",
                    "программа 1 канала на сегодня", "программа телепередач на сегодня все каналы",
                    "тв программа на сегодня все каналы", "программа передач все каналы",
                    "программа передач на сегодня все каналы", "программа передач 1 канал",
                    "программа передач на сегодня 1 канал", "программа передач все каналы москва", "1 канал программа",
                    "программа 1 канала на сегодня", "программа передач 1 канал",
                    "программа передач на сегодня 1 канал", "канал россия 1 программа", "первый канал программа",
                    "программа первый первом канале", "программа передач первый канал",
                    "первый канал программа на сегодня", "первый канал программа передач на сегодня",
                    "программа первый первом канале", "программа первого канала", "программа передач первого канала",
                    "программа первого канала на сегодня", "программа передач первого канала на сегодня",
                    "программа телепередач все каналы", "программа телепередач на сегодня все каналы",
                    "тв программа все каналы", "тв программа на сегодня все каналы", "тв программа 1 канал",
                    "канал москва программа", "программа на сегодня все каналы москва",
                    "программа передач все каналы москва", "программа передач москва на сегодня все каналы",
                    "канал россия программа", "канал россия 1 программа", "канал россия программа на сегодня",
                    "программа передач канал россия", "канал россия 1 программа передач", "канал март программа",
                    "программа 1 канала 1 марта", "смотреть программу канал", "программа смотреть каналы онлайн",
                    "программа канала смотреть бесплатно", "смотреть программу канала время",
                    "программа смотреть каналы онлайн бесплатно", "программа канала дом кино",
                    "программа канала русское кино", "программа канала кино 1000", "программа канала кино на неделю",
                    "программа канала 1000 русское кино", "программа канала русский", "программа канала русский роман",
                    "канал русский бестселлер программа", "программа канала русское кино",
                    "программа канала русский детектив"]
tv_info = ["телеведущие", "телеведущие биография", "фото телеведущих", "телеведущие ольги", "голы телеведущие",
           "фото телеведущих",
           "фото телеведущих в купальнике", "дети телеведущих фото", "личные фото телеведущих",
           "фото голых телеведущих",
           "телеведущие ольги", "телеведущие ольга белова", "телеведущие биография",
           "телеведущие биография личная жизнь", "телеведущие канала", "телеведущие 1 канала",
           "телеведущие первого канала", "первыйканал телеведущие", "телеведущие личная жизнь",
           "телеведущие биография личная жизнь", "дмитрий борисов телеведущий личная",
           "дмитрий борисов телеведущий личная жизнь", "личные фото телеведущих"]

tv_provider = ["как подключить цифровое телевидение", "как подключить цифровое телевидение к телевизору",
               "подключить каналы цифрового телевидения", "как подключить приставку цифрового телевидения",
               "как подключить приставку цифрового телевидения к телевизору", "подключить кабельное телевидение",
               "как подключить кабельное телевидение к телевизору", "какое кабельное телевидение подключить",
               "подключить цифровое кабельное телевидение", "можно ли подключить кабельное телевидение",
               "как подключить телевидение к телевизору", "как подключить цифровое телевидение к телевизору",
               "как подключить приставку цифрового телевидения к телевизору",
               "как подключить кабельное телевидение к телевизору",
               "как подключить телевидение ростелеком к телевизору", "как подключить приставку цифрового телевидения",
               "как подключить приставку цифрового телевидения к телевизору", "подключить телевидение без приставки",
               "подключить цифровое телевидение без приставки",
               "приставки для приема цифрового телевидения как подключить", "ростелеком подключить телевидение",
               "ростелеком подключить интернет и телевидение", "как подключить телевидение ростелеком к телевизору",
               "как подключить интерактивное телевидение ростелеком", "ростелеком подключить телевидение цена",
               "подключить каналы телевидения", "подключить каналы цифрового телевидения",
               "когда подключат 20 каналов на цифровое телевидение", "бесплатное телевидение 20 каналов как подключить",
               "цифровое телевидение бесплатные каналы как подключить", "какое телевидение подключить",
               "какое телевидение лучше подключить", "какое кабельное телевидение подключить",
               "какое телевидение можно подключить", "какое цифровое телевидение подключить", "как подключить смарт тв",
               "как подключить смарт тв самсунг", "как подключить смарт тв к интернету", "как подключить смарт тв wifi",
               "как подключить смарт тв через wifi", "подключить триколор тв", "триколор тв интернет как подключить",
               "как подключить триколор тв к телевизору", "подключим ресивер триколор тв",
               "триколор тв подключить каналы"]

tv_setup = ["как настроить каналы на телевизоре", "как настроить телевизор на цифровые каналы",
            "как настроить каналы на телевизоре самсунг", "как настроить каналы на телевизоре lg",
            "телевизор самсунг как настроить цифровые каналы", "настрою телевизор самсунг", "настрою телевизор самсунг",
            "как настроить телевизор самсунг", "как настроить каналы на телевизоре самсунг",
            "как настроить телевизор самсунг на цифровое", "как настроить телевизор самсунг смарт",
            "как настроить телевизор lg", "как настроить каналы на телевизоре lg", "как настроить телевизор lg тв",
            "настроить телевизор lg на цифровое", "как настроить телевизор lg смарт",
            "как настроить телевизор на цифровые", "как настроить телевизор на цифровые каналы",
            "как настроить цифровое телевидение на телевизоре", "как настроить телевизор самсунг на цифровое",
            "телевизор самсунг как настроить цифровые каналы"]

common = ["телевидение", "тв"]

common.extend(common)
common.extend(tv_info)
common.extend(watch_tv_program)
common.extend(watch_tv_online)
common.extend(tv_provider)
common.extend(tv_setup)


def find_stuff(line, words):
    count = 0
    for word in words:
        count += line.find(word)
    if count > 0:
        return True
    else:
        return False


def count_lines(f):
    count = 0
    with open(f) as fa:
        for l in fa:
            count += 1
    return count


def do_the_magic(words):
    count = 0
    with open(filename) as f:
        tv_file = open('tv', 'w')
        for line in f:
            if find_stuff(line, words):
                count = count + 1
                tv_file.write(line)
        tv_file.close()
    filecount = count_lines(filename)
    print('File contains: {} lines'.format(filecount))
    print('File contains: {} target lines'.format(count))
    print('Similarity percent is: {}'.format(count / float(filecount)))


def main():
    print("watch_tv_online")
    do_the_magic(watch_tv_online)
    print()

    print("watch_tv_program")
    do_the_magic(watch_tv_program)
    print()

    print("tv_info")
    do_the_magic(tv_info)
    print()

    print("tv_provider")
    do_the_magic(tv_provider)
    print()

    print("tv_setup")
    do_the_magic(tv_setup)
    print()

    print("common search")
    do_the_magic(common)


if __name__ == "__main__":
    main()
