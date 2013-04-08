# -*- coding: utf-8 -*-
#Config for Serial Logger v3.3

#Зависти от OS. Для win вида COM1... для *nix /dev/tty*

#Вовкина
#SERIAL_PORT = '/dev/tty.usbserial-A600dAzt'

#Моя nano
SERIAL_PORT = '/dev/tty.SLAB_USBtoUART'

#SERIAL_PORT = 'COM3'

#Допустимые значения 300, 1200, 2400, 4800, 14400, 19200, 28800, 38400, 57600, 115200. Рекомендовано 9600. Согласовано с прошивкой контроллера.
SERIAL_SPEED = 9600

#Допустимые значения win или unix
#OS_TYPE = 'win'