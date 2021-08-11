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


from lib import check_status
from lib import get_links
import random
import time
import webbrowser
import winsound


# Выбор консоли
search_mode = input('\nВыберите консоль (введите число и нажмите Enter):\n1 - Xbox Series X\n2 - Xbox Series S\n')
while True:
    if search_mode == '1':
        print('\nВыбрана Xbox Series X')
        target_links = get_links.get_xsx_links()
        break
    elif search_mode == '2':
        print('\nВыбрана Xbox Series S')
        target_links = get_links.get_xss_links()
        break
    else:
        search_mode = input('\nВыберите консоль (введите число и нажмите Enter):\n1 - Xbox Series X\n2 - Xbox Series S\n')

# Проверка наличия консоли
exit_flag = False
while True:
    print(f'\n{time.strftime("%H:%M:%S", time.localtime())}')
    for shop, url in target_links.items():
        result = check_status.check_status(url)
        if result:
            print(f'{shop:.<20}' + f'{check_status.status_message():.>30}')
            lucky_url = url
            exit_flag = True
            break
        else:
            print(f'{shop:.<20}' + f'{check_status.status_message():.>30}')
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
