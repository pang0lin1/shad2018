# -*- coding: utf-8 -*-

filename = 'Log'
list_1 = ["телевидение"]
list_2 = ["телепередача"] # нужно сделать, чтобы искал по всем словоформам и склонениям (?)
list_3 = ["тв"]
list_4 = ["смотреть онлайн"] # возможно допилить поиск не в зависимости от порядка слов в элементе (?)
list_5 = ["tv"]
lists_total = [""]

# делаю список lists_total со всеми запросами про телевидение. Получилось около 16% от запросов лога
lists_total.extend(list_1)
lists_total.extend(list_2)
lists_total.extend(list_3)
lists_total.extend(list_4)
lists_total.extend(list_5)

# считаю сколько раз встречается слово
def find_stuff(line, words):
    count = 0
    for word in words:
        count += line.find(word)
    if count > 0:
        return True
    else:
        return False

# считаю сколько всего строк в логе запросов
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
    print('Доля группы запросов в логе {}'.format(count / float(filecount)))


def main():
    print("1")
    do_the_magic(list_1)
    print

    print("2")
    do_the_magic(list_2)
    print

    print("3")
    do_the_magic(list_3)
    print

    print("4")
    do_the_magic(list_4)
    print

    print("5")
    do_the_magic(list_5)
    print

    print("total")
    do_the_magic(lists_total)


if __name__ == "__main__":
    main()

# нужно посчитать долю группы запросов в объеме телевизионных запросов (процент от lists_total)
# надо прикрутить matplotlib и визуализировать доли запросов
# сделать, чтобы искал только в куске url с запросом, то есть после "text="