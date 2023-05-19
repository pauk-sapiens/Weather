#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os


def get_html():
    url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9E%D0%B4%D0%B8%D0%BD%D1%86%D0%BE%D0%B2%D0%BE,_%D0%9E%D0%B4%D0%B8%D0%BD%D1%86%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD'
    r = requests.get(url)
    return r.text


def get_degrees(html):
    soup = BeautifulSoup(html, features='html.parser')
    t = soup.findAll('span', {'class': 't_0'})
    return t[2].text

    
def notify(message):
    title = 'Погода в Одинцово'
    os.system('notify-send "{}" "{}"'.format(title, message))


def main():
    degrees=get_degrees(get_html())
    notify(degrees)



if __name__ == '__main__':
    main()


