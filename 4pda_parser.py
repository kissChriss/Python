# парсинг подфорумов сайта http://4pda.ru 
# с их последующей сортировкой по темам и ответам

from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs

html = urlopen('http://4pda.ru/forum/index.php?showforum=281')

resp = bs(html, 'html.parser')
table = resp.find('table', class_='ipbtable')

projects = []

for rows in table.find_all('tr')[1:]:
    cols = rows.find_all('td')
    projects.append({
        'Форум': cols[1].a.text,
        'Тем:': int(cols[2].text),
        'Ответов:': int(cols[3].text)
    })

print('Прямой вывод')
for project in projects:
    print(project)

print()

print('Сортировка по темам')
sort_themes = sorted(projects, key=lambda d: d['Тем:'], reverse=True)
for thms in sort_themes:
    print(thms)

print()

print('Сортировка по ответам')
sort_answers = sorted(projects, key=lambda d: d['Ответов:'], reverse=True)
for answ in sort_answers:
    print(answ) 
