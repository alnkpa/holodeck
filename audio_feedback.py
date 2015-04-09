#!/usr/bin/env python

import pygame.mixer
import socket
import os

soundName = lambda s: os.path.join("data", s) + ".wav")
sound = lambda s: pygame.mixer.Sound(soundName(s))

pygame.mixer.init()

bump = sound("Bump")
ding = sound("Ding")
noise = sound("Buzz")

# Sounds generated with 
#   say -r 0.7 '0--A' -o 0a.aiff
#   ffmpeg -i 0a.aiff 0a.wav
numbers = map(str, range(9)) + ["U"]
letters = ['', 'a', 'b', 'c', 'd', 'e', 'f']

numbersounds = {k: sound(k) for k in (n+l for n in numbers for l in letters)}

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
			number = data.partition("Bump")[2].strip().lower()
			numbersounds[number].play()
			bump.play()
		elif data.startswith("Move"):
			number = data.partition("Move")[2].strip().lower()
			numbersounds[number].play()
		elif data.startswith("END"):
			break
	except KeyboardInterrupt:
		break
	except:
		pass

