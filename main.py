import bs4
import requests
from fake_user_agent import user_agent


def scraping(words):
    url = 'https://habr.com/ru/all'
    response = requests.get(url, headers={'User-Agent': user_agent()})
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')
    for article in articles:
        datetime = article.find(class_='tm-article-datetime-published').find('time').attrs['title']
        date = datetime.split(',')[0]
        title = article.find(class_="tm-article-snippet__title-link").find('span').text
        href = article.find(class_="tm-article-snippet__title-link").attrs['href']
        full_href = f'{url}{href}'
        text = article.text
        if any([keyword in text or keyword.capitalize() in text for keyword in words]):
            print(f'{date} - {title} - {full_href}')


if __name__ == '__main__':
    keywords = ['бубен', 'unity', 'web', 'python']
    scraping(keywords)
