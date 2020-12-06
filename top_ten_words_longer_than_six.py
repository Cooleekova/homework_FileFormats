
# создаю функцию words_count, которая обходит циклом список слов,
# все слова длиннее шести символов сохраняет в словарь, где ключом
# становится количество повторений слова, а значением по ключу само слово.
# ключи словаря сортируются по убыванию, их значения выводятся в новый список top_ten

def words_count(news):
    news_dict = dict()
    top_ten = list()
    for word in news:
        if len(word) > 6:
        # if len(word) >= 6: из задания было неясно, включать ли слова из шести букв в ТОП
            news_dict[news.count(word)] = word
            freq = sorted(list(news_dict.keys()), reverse = True)
    for k, v in news_dict.items():
        if k in (freq[0:11]):
            top_ten.extend(v.split())
    return top_ten

# программа для файла в формате json

import json

# открываю файл,
# по ключу items нахожу список словарей с новостями

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)
    json_news = json_data['rss']['channel']['items']

# создаю пустой список и складываю в него все слова,
# входящие в описание каждой новости.
# в каждом словаре это текстовое значение по ключу description

    all_news_json = list()
    for item in json_news:
        all_news_json.extend(item['description'].split())

# вызываю функцию words_count для списка слов, полученного из файла json

print(f'ТОП 10 самых повторяющихся слов длиннее шести символов в файле {f.name}:\n {words_count(all_news_json)}')


# программа для файла в формате XML

# открываю файл
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)

# с помощью tree.getroot() нахожу основной тег

root = tree.getroot()

# c помощью root.findall() получаю новости <item>,
# расположенные под тегом <channel>

xml_data = root.findall('channel/item')

# создаю пустой список и складываю в него все слова,
# входящие в описание каждой новости.
# описание новостей находится в тексте <description> под каждым тегом <item>

all_news_xml = list()
for news in xml_data:
    all_news_xml.extend((news.find('description').text).split())

# вызываю функцию words_count для списка слов, полученного из файла xml

print(f'ТОП 10 самых повторяющихся слов длиннее шести символов в файле XML:\n {words_count(all_news_xml)}')