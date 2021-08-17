# This file is part of XboxHunter project.
# Copyright (C) 2021 Evgeniy Ipatov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


from bs4 import BeautifulSoup as bSoup
import certifi
import requests
from requests_html import HTMLSession


__status_message = ''


def check_status(target_url: str) -> bool:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    global __status_message
    __status_message = ''
    try:
        if 'https://xn--d1aiavecq8cxb.xn--p1ai' in target_url:
            session = HTMLSession()
            response = session.get(target_url, headers=headers, timeout=30, verify=certifi.where())
        else:
            response = requests.get(target_url, headers=headers, timeout=30, verify=certifi.where())
    except:
        __status_message = 'Ошибка запроса'
        return False
    if not response.ok:
        __status_message = 'Отказано в доступе'
        return False
    if 'https://xn--d1aiavecq8cxb.xn--p1ai' in target_url:
        response.html.render(timeout=60)
        parsed_page = bSoup(response.html.html, 'html.parser')
    else:
        parsed_page = bSoup(response.text, 'html.parser')

    if 'mvideo.ru' in target_url:
        result = False

    elif 'eldorado.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('a', class_='gs-avail-btn item_subscription_link no-mobile')]
        result = len(data) == 0

    elif 'dns-shop.ru' in target_url:
        result = False

    elif 'citilink.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('span', class_='Button__text jsButton__text')]
        result = '\n                В корзину\n            ' in data

    elif 'ozon.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('div', class_='kxa6')]
        result = 'Добавить в корзину' in data

    elif 'svyaznoy.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('span', class_='b-main-btn__text')]
        result = 'Ð\x9aÑ\x83Ð¿Ð¸Ñ\x82Ñ\x8c' in data

    elif 'sbermegamarket.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('button', class_='buy-button__button btn sm btn-block')]
        result = 'Ð\x9aÑ\x83Ð¿Ð¸Ñ\x82Ñ\x8c' in data

    elif 'megafon.ru' in target_url:
        result = False

    elif 'gamepark.ru' in target_url:
        data_1 = [element.text for element in parsed_page.find_all('a', class_='subscribe_no_by modal_link')]
        result_1 = not 'Узнать о наличии' in data_1
        data_2 = [element.text for element in parsed_page.find_all('a', class_='book_now is_magazin modal_link')]
        result_2 = 'Только в магазине' in data_2
        result = result_1 or result_2

    elif 'technopark.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('span', class_='buy')]
        result = 'Купить' in data

    # подпишись.рф
    elif 'xn--d1aiavecq8cxb.xn--p1ai' in target_url:
        data = [element.text for element in parsed_page.find_all('button', class_='btn btn-lg btn-rounded btn-order mb-sm-3')]
        result = 'Оформить заявку' in data

    elif 'computeruniverse.net' in target_url:
        result = False

    elif 'kcentr.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('a', class_='product-cart _card jsAddToCart btn _block _red')]
        result = ' Добавить в корзину' in data

    elif '1c-interes.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('a', class_='btn_order product_buy_button btn btn_orange retailRocket-bakset-btn order-link')]
        result = '\nВ корзину\n' in data

    elif 'onlinetrade.ru' in target_url:
        data = [element.text for element in parsed_page.find_all('h3')]
        result = not 'Снят с продажи' in data

    else:
        result = False

    if result:
        __status_message = 'Есть в наличии'
    else:
        __status_message = 'Нет в наличии'
    
    return result


def status_message() -> str:
    return __status_message
