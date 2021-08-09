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


import check_status
import random
import time
import webbrowser
import winsound


# Список ссылок на консоли в различных магазинах
xbox_series_x_links = {
'М.видео': 'https://www.mvideo.ru/products/igrovaya-pristavka-microsoft-xbox-series-x-40073271',
'Эльдорадо': 'https://www.eldorado.ru/cat/detail/igrovaya-pristavka-microsoft-xbox-series-x/',
#'DNS': 'https://www.dns-shop.ru/product/2e0abd026fcb1b80/igrovaa-konsol-microsoft-xbox-series-x/',
'Ситилинк': 'https://www.citilink.ru/product/igrovaya-konsol-microsoft-xbox-series-x-rrt-00011-chernyi-1434349/',
#'Ozon': 'https://www.ozon.ru/product/igrovaya-konsol-microsoft-xbox-series-x-chernyy-173667655/',
'Связной': 'https://www.svyaznoy.ru/catalog/gamepad/9209/5835083',
'Сбермегамаркет': 'https://sbermegamarket.ru/catalog/details/igrovaya-pristavka-microsoft-xbox-series-x-100027479079/',
#'Мегафон': 'https://shop.megafon.ru/toys/135796.html',
'Gamepark': 'https://www.gamepark.ru/xboxone/console/IgrovayakonsolXboxSeriesX/',
'Technopark': 'https://www.technopark.ru/igrovaya-pristavka-microsoft-xbox-series-x-1tb/',
#'Подпишись.РФ': 'https://подпишись.рф/catalog/XBOX_Series_X/8569'
}
xbox_series_s_links = {
'М.видео': 'https://www.mvideo.ru/products/igrovaya-pristavka-microsoft-xbox-series-s-512gb-40074462',
'Эльдорадо': 'https://www.eldorado.ru/cat/detail/igrovaya-pristavka-microsoft-xbox-series-s-512gb/',
#'DNS': 'https://www.dns-shop.ru/product/fc4f8bb2f2fc3332/igrovaa-konsol-microsoft-xbox-series-s/',
'Ситилинк': 'https://www.citilink.ru/product/igrovaya-konsol-microsoft-xbox-series-s-rrs-00011-belyi-1434347/',
#'Ozon': 'https://www.ozon.ru/product/igrovaya-konsol-microsoft-xbox-series-s-belyy-226110788/',
'Связной': 'https://www.svyaznoy.ru/catalog/gamepad/9209/5835086',
'Сбермегамаркет': 'https://sbermegamarket.ru/catalog/details/igrovaya-pristavka-microsoft-xbox-series-s-100027479080/',
#'Мегафон': 'https://shop.megafon.ru/toys/135797.html',
'Gamepark': 'https://www.gamepark.ru/xboxone/console/IgrovayakonsolXboxSeriesS/',
'Technopark': 'https://www.technopark.ru/igrovaya-pristavka-microsoft-xbox-series-s-512gb/',
#'Подпишись.РФ': 'https://подпишись.рф/catalog/XBOX_Series_S/8568'
}

# Выбор консоли
search_mode = input('\nВыберите консоль (введите число и нажмите Enter):\n1 - Xbox Series X\n2 - Xbox Series S\n')
while True:
    if search_mode == '1':
        print('\nВыбрана Xbox Series X')
        target_links = xbox_series_x_links
        break
    elif search_mode == '2':
        print('\nВыбрана Xbox Series S')
        target_links = xbox_series_s_links
        break
    else:
        search_mode = input('\nВыберите консоль (введите число и нажмите Enter):\n1 - Xbox Series X\n2 - Xbox Series S\n')

# Проверка наличия консоли
exit_flag = False
while True:
    print(time.strftime('%H:%M:%S', time.localtime()))
    for shop, url in target_links.items():
        result = check_status.check_status(shop, url)
        if result:
            print(f'{shop}: Есть в наличии')
            lucky_url = url
            exit_flag = True
            break
        else:
            print(f'{shop}: Нет в наличии')
    if exit_flag:
        break
    else:
        delay = random.randint(60, 180)
        time.sleep(delay)

# Открытие ссылки в браузере
webbrowser.open_new_tab(lucky_url)

# Подача звукового сигнала
for index in range(0, 100):
    winsound.Beep(800, 1000)
user_answer = input()
