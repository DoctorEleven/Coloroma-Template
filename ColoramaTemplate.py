#!/usr/bin/python3
# -*- coding: utf-8 -*-
from colorama import *
init(autoreset=True)


cores=[Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
cores2=[Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
estilo=[Style.DIM, Style.NORMAL, Style.BRIGHT]


for item in estilo:
	print(item+"	Testando cores. ".center(30,'#'))
print("")

for item in cores:
	for item2 in cores2:
		print(item2+item+"	Testando cores. ".center(30,'#'))
print("")


'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''


