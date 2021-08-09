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


def check_status(shop_name: str, target_url: str) -> bool:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
    try:
        response = requests.get(target_url, headers=headers, verify=certifi.where())
    except:
        return False
    if not response.ok:
        return False
    parsed_page = bSoup(response.text, 'html.parser')

    if shop_name == 'М.видео':
        result = [element.text for element in parsed_page.find_all('div', class_='fl-pdp-pay__sales-start-date-label')]
        return not '\n                    Скоро в продаже\n ' in result

    elif shop_name == 'Эльдорадо':
        result = [element.text for element in parsed_page.find_all('span', class_='gtmAddToBasket addToCartBigCP cartButtonText')]
        return 'Добавить в корзину' in result

    #elif shop_name == 'DNS':
        #pass

    elif shop_name == 'Ситилинк':
        result = [element.text for element in parsed_page.find_all('span', class_='Button__text jsButton__text')]
        return '\n                В корзину\n            ' in result

    elif shop_name == 'Ozon':
        result = [element.text for element in parsed_page.find_all('div', class_='kxa6')]
        return 'Добавить в корзину' in result

    elif shop_name == 'Связной':
        result = [element.text for element in parsed_page.find_all('span', class_='b-main-btn__text')]
        return 'Ð\x9aÑ\x83Ð¿Ð¸Ñ\x82Ñ\x8c' in result

    elif shop_name == 'Сбермегамаркет':
        result = [element.text for element in parsed_page.find_all('button', class_='buy-button__button btn sm btn-block')]
        return 'Ð\x9aÑ\x83Ð¿Ð¸Ñ\x82Ñ\x8c' in result

    #elif shop_name == 'Мегафон':
        #pass

    elif shop_name == 'Gamepark':
        result = [element.text for element in parsed_page.find_all('a', class_='subscribe_no_by modal_link')]
        return not 'Узнать о наличии' in result

    elif shop_name == 'Technopark':
        result = [element.text for element in parsed_page.find_all('span', class_='buy')]
        return 'Купить' in result

    #elif shop_name == 'Подпишись.РФ':
        #pass

    else:
        return False
