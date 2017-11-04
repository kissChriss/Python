from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv

filename_themes = 'themes.csv'
filename_answers = 'answers.csv'

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

sort_themes = sorted(projects, key=lambda d: d['Тем:'], reverse=True)
sort_answers = sorted(projects, key=lambda d: d['Ответов:'], reverse=True)

with open (filename_themes, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('Форум', 'Тем', 'Ответов'))
    for thms in sort_themes:
        writer.writerow((thms['Форум'], thms['Тем:'], thms['Ответов:']))

with open(filename_answers, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('Форум', 'Тем', 'Ответов'))
    for answ in sort_answers:
        writer.writerow((answ['Форум'], answ['Тем:'], answ['Ответов:']))



