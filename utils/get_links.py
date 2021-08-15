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


import pathlib


def __get_links(folder_name: str) -> dict:
    # Выбор файлов с расширением txt
    p = pathlib.Path('.').parent / folder_name
    p = p.glob('*.txt')
    file_names = sorted([name for name in p if name.is_file()])
    result = {}
    for name in file_names:
        try:
            with open(name, 'rt') as input:
                result[name.stem] = input.readline().replace('\n', '')
        except:
            pass
    return result


def get_xsx_links() -> dict:
    return __get_links('xsx_links')


def get_xss_links() -> dict:
    return __get_links('xss_links')
