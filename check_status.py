# Программа для мониторинга наличия Xbox Series X/S в магазинах
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

__status_message = ''

def check_status(shop_name: str, target_url: str) -> bool:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    global __status_message
    __status_message = ''
    try:
        response = requests.get(target_url, headers=headers, timeout=10, verify=certifi.where())
    except:
        __status_message = 'Отказано в доступе'
        return False
    if not response.ok:
        __status_message = 'Отказано в доступе'
        return False
    parsed_page = bSoup(response.text, 'html.parser')

    if shop_name == 'М.видео':
        data = [element.text for element in parsed_page.find_all('div', class_='fl-pdp-pay__sales-start-date-label')]
        result = not '\n                    Скоро в продаже\n ' in data

    elif shop_name == 'Эльдорадо':
        data = [element.text for element in parsed_page.find_all('span', class_='gtmAddToBasket addToCartBigCP cartButtonText')]
        result = 'Добавить в корзину' in data

    #elif shop_name == 'DNS':
        #pass

    elif shop_name == 'Ситилинк':
        data = [element.text for element in parsed_page.find_all('span', class_='Button__text jsButton__text')]
        result = '\n                В корзину\n            ' in data

    elif shop_name == 'Ozon':
        data = [element.text for element in parsed_page.find_all('div', class_='kxa6')]
        result = 'Добавить в корзину' in data

    elif shop_name == 'Связной':
        data = [element.text for element in parsed_page.find_all('span', class_='b-main-btn__text')]
        result = 'Ð\x9aÑ\x83Ð¿Ð¸Ñ\x82Ñ\x8c' in data

    elif shop_name == 'Сбермегамаркет':
        data = [element.text for element in parsed_page.find_all('button', class_='buy-button__button btn sm btn-block')]
        result = 'Ð\x9aÑ\x83Ð¿Ð¸Ñ\x82Ñ\x8c' in data

    #elif shop_name == 'Мегафон':
        #pass

    elif shop_name == 'Gamepark':
        data_1 = [element.text for element in parsed_page.find_all('a', class_='subscribe_no_by modal_link')]
        result_1 = not 'Узнать о наличии' in data_1
        data_2 = [element.text for element in parsed_page.find_all('a', class_='book_now is_magazin modal_link')]
        result_2 = 'Только в магазине' in data_2
        result = result_1 or result_2

    elif shop_name == 'Technopark':
        data = [element.text for element in parsed_page.find_all('span', class_='buy')]
        result = 'Купить' in data

    #elif shop_name == 'Подпишись.РФ':
        #pass

    else:
        result = False

    if result:
        __status_message = 'Есть в наличии'
    else:
        __status_message = 'Нет в наличии'
    
    return result

def status_message() -> str:
    return __status_message
