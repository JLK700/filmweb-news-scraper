from bs4 import BeautifulSoup
import requests
import json


def scrape_filmweb_article(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    typ_of_news = soup.find(class_='newsHeaderSection__type').text
    date = soup.find(class_='newsHeaderSection__date tooltip__parent').text
    text = soup.findAll(class_='page__text')[2].text
    title = soup.find(class_='newsHeaderSection__title').text

    return title, typ_of_news, date, text


def get_news_from_filmweb_page(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    result = ['https://www.filmweb.pl' + url['href'] for url in soup.findAll(class_="thumbnail__link")]

    return result[0:18]


def get_all_urls_from_many_filmweb_pages(start, end):
    url = 'https://www.filmweb.pl/news?page='
    result = []
    for page in range(start, end):
        result += get_news_from_filmweb_page(url + str(page))
    return result


def scrape(*, page_start, page_end):
    my_dict = {}
    url_list = get_all_urls_from_many_filmweb_pages(start=page_start, end=page_end)
    for i, url in enumerate(url_list):
        title, typ_of_news, date, text = scrape_filmweb_article(url)
        my_dict[i] = {'title': title, 'type:': typ_of_news, 'date': date, 'text': text}
        print("done: " + str(i / len(url_list)))

    with open('corpus.json', 'w') as json_file:
        json.dump(my_dict, json_file)


# Example usage
scrape(page_start=1, page_end=2)
