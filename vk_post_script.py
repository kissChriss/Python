#automatical news posting for vk.com from 4pda.ru

from requests import *
from bs4 import BeautifulSoup as bs
import vk_requests

api = vk_requests.create_api(
    service_token='yourToken')

def get_html(url):
    response = get(url)
    return response.text

def main():
    BASE_URL = 'http://4pda.ru/news/page/'
    for i in range(1,2):
        url = BASE_URL + str(i)
        soup = bs(get_html(url), 'html.parser')
        articles = soup.find_all('article', class_ = 'post')
        posts = []

        for article in articles:
                posts.append({
                    'name': article.find('a')['title'],
                    'comments': int(article.find('a', class_ = 'v-count').text),
                    'date': article.find('em', class_='date').text,
                    'post_url': article.find('a')['href'],
                    'text': article.find('p').text
                })

        sorted_comments = sorted(posts, key=lambda d: d['comments'], reverse=True)

        i = 0
        name = posts[i]['name']
        comms = '\nБолее ' + str(sorted_comments[i]['comments']) + ' comments'
        text = '\n\n' + sorted_comments[i]['text']
        post_url = 'http:' + sorted_comments[i]['post_url'][:27]
        
        message = name  + comms + text + '\n#4pda@fox_it_news' + '\n#news'
        api.wall.post(owner_id='groupId', message= message, attachments = post_url, scope = 'offline')


if __name__ == '__main__':
    main()
