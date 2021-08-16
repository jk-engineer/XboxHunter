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


from getpass import getpass
from email.message import EmailMessage
import smtplib


class EmailNotity():


    def __init__(self) -> None:
        self.__from_email = input('\nВведите адрес электронной почты (поддерживается только gmail), с которой будут отправляться уведомления:\n')
        self.__email_password = getpass('\nВведите пароль электронной почты, указанной выше:\n')
        self.__to_email = input('\nВведите адрес электронной почты, на которую будет отправлено уведомление:\n')
        self.send_start_message()


    def __send_message(self, message_content: str):
        # Создание сообщения
        msg = EmailMessage()
        msg['Subject'] = 'XboxHunter'
        msg['From'] = self.__from_email
        msg['To'] = self.__to_email
        msg.set_content(message_content)
        # Отправка сообщения
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.ehlo()
            server.login(self.__from_email, self.__email_password)
            server.send_message(msg)
            server.close()
            print('\nУведомление отправлено')
        except Exception as error:
            print('\nОшибка отправки уведомления:\n', error)


    def send_start_message(self):
        self.__send_message('Запущена программа XboxHunter. Ожидайте уведомление со ссылкой.')


    def send_success_message(self, lucky_url: str):
        self.__send_message(lucky_url)
