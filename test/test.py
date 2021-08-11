# Программа для тестирования
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


from ..lib import check_status


links = {
'DNS': 'https://www.dns-shop.ru/product/d0a91343aa2f3332/653-smartfon-xiaomi-redmi-9-64-gb-seryj/',
'Ситилинк': 'https://www.citilink.ru/product/smartfon-xiaomi-redmi-9-64gb-4gb-seryi-3g-4g-6-53-and10-wifi-nfc-gps-1391508/',
'МВидео': 'https://www.mvideo.ru/products/smartfon-xiaomi-redmi-9-464gb-carbon-grey-30050582',
'Эльдорадо': 'https://www.eldorado.ru/cat/detail/smartfon-redmi-9-4-64gb-carbon-grey/',
'Ozon': 'https://www.ozon.ru/product/smartfon-note10-pro-siniy-296727025/',
'Связной': 'https://www.svyaznoy.ru/catalog/phone/224/5787482',
'Сбермегамаркет': 'https://sbermegamarket.ru/catalog/details/smartfon-redmi-9-464gb-carbon-grey-100026886795/',
'Мегафон': 'https://kirov.shop.megafon.ru/mobile/133985.html',
'Gamepark': 'https://www.gamepark.ru/xboxone/games/Cyberpunk2077XboxOne/',
'Technopark': 'https://www.technopark.ru/smartfon-xiaomi-redmi-note-9-64gb-lesnoy-zelenyy/',
'Подпишись.РФ': 'https://подпишись.рф/catalog/Samsung_Galaxy_S21/SM-G991BZVDSER',
'Computeruniverse': 'https://www.computeruniverse.net/ru/p/90825717'
}

for shop, url in links.items():
    print(f'{shop}: {check_status.check_status(shop, url)}')
