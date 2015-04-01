#!/usr/bin/env python

import pygame.mixer
import socket

pygame.mixer.init()

bump = pygame.mixer.Sound(u"Bump.wav")
ding = pygame.mixer.Sound(u"Ding.wav")
noise = pygame.mixer.Sound(u"Buzz.wav")

numbers = map(str, range(9)) + ["U"]
letters = ['', 'a', 'b', 'c', 'd', 'e', 'f']

numbersounds = {k: pygame.mixer.Sound(k + ".wav") for k in (n+l for n in numbers for l in letters)}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 29999))


while True:
	try:
		data = sock.recv(1024)
		print data
		if data.startswith("STOP"):
			noise.stop()
		elif data.startswith("START"):
			noise.play(loops=-1)
		elif data.startswith("Bump"):
			number = data.partition("Bump")[2].strip()
			numbersounds[number].play()
			bump.play()
		elif data.startswith("Move"):
			number = data.partition("Move")[2].strip()
			numbersounds[number].play()
		elif data.startswith("END"):
			break
	except KeyboardInterrupt:
		break
	except:
		pass

