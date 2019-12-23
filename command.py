#!/usr/bin/python
__author__ = 'BlackCat'
import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

if total > 1:
	command = str(sys.argv[1])
	if command == "bark":
		print('Bark')
	if command == "attack":
		print('I will kill you')
	if command == "luc":
		print('I am your father')

