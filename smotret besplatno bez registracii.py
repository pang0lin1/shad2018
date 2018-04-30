import pandas as pd
from collections import Counter
import numpy as np
import sys

# Загрузим данные

data = pd.read_table(sys.argv[1], encoding='utf-8')

# Выделим запросы без url

url_part = "https://yandex.ru/search/?text="
data["reduced_request"] = data["request"].apply(lambda x: x[len(url_part):])

# Теперь избавимся от лишних символов в конце запроса

data["reduced_request"] = data["reduced_request"].apply(lambda x: x[:x.find("&")] if "&" in x else x)

# Приведем все строки к нижнему регистру

data["reduced_request"] = data["reduced_request"].apply(lambda x: x.lower())

# Проведем "наивную" классификацию запросов, связанных с телевидением. Для этого составим словари с ключевыми словами
# direct - прямые запросы,
# channels - тв каналы,
# celeb - тв знаменитости,
# prog - тв передачи,
# connect - подключение тв

request_dict = {"direct": ["телевидение", "телевидении", "телевидения", "телевидению",
                           " tv ", "-tv", "tv-", " тв ", "-тв", "тв-", "ntktdbltybt"],
               "channels": ["телеканал", "канал", "rfyfk", " стс ", " орт ", " нтв ", "рен тв", " тнт ",
                           " стс", " орт", " нтв", " рентв", " тнт","орт ", "нтв ", "тнт ", "стс ", " ртр ", " ртр", "ртр "
                            "матч тв", "спорт тв", "россия 1", "россия1", "музтв", "муз тв"],
               "celeb": ["максим дахненко", "комаров дмитрий", "елена степаненко", "яна рудковская", "ольга бузова",
                         "дмитрий нагиев", "светлаков", "светлаков", "малахов", "батрутдинов", "канделаки", "ургант"],
               "prog": ["камеди", "comedy", "воскресный вечер", "вести недели", "давай поженимся", "топ гир", "пусть говорят",
                       "ревизорро", "битва экстасенсов", "дом 2", "вечерний ургант", "жди меня", "танцы со звездами",
                        "орел и решка"],
               "connect": ["спутниковое", "кабельное", "эфир"]}
request_class_dict = {"direct": [], "channels": [], "celeb": [], "prog": [], "connect": []}
for key in request_dict.keys():
    for value in request_dict[key]:
        request_class_dict[key].append(data[data["reduced_request"].str.contains(value)]["reduced_request"])

# Теперь оценим долю запросов, связанных с телевидением в общем потоке. Учтем, что запросы в разных классах могут повторяться

tv_queries_list = []
for key in request_class_dict.keys():
    for value in request_class_dict[key]:
        tv_queries_list += value.tolist()

#длина списка запросов без повторений

unique_tv_queries = len(np.unique(tv_queries_list))

# Доля запросов, связанных с телевидением, в общем потоке запросов, %

print("Доля запросов, связанных с телевидением, в общем потоке запросов, %", float(unique_tv_queries)/data.shape[0]*100)

# Оценим теперь долю каждого класса в запросах, связанных с телевидением

for key in request_class_dict.keys():
    class_queries_list = []
    for value in request_class_dict[key]:
        class_queries_list += value.tolist()
    print("Доля "+key, float(len(np.unique(class_queries_list)))/unique_tv_queries*100,"%")

