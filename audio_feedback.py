#!/usr/bin/env python

import pygame.mixer
import socket
import os

pygame.mixer.init()

soundName = lambda s: os.path.join("data", s) + ".wav"
sound = lambda s: pygame.mixer.Sound(soundName(s))

load = lambda s: pygame.mixer.music.load

bump = sound("Bump")
ding = sound("Ding")
noise = sound("Buzz")

# Sounds generated with 
#   say -r 0.7 '0--A' -o 0a.aiff
#   ffmpeg -i 0a.aiff 0a.wav
numbers = map(str, range(10)) + ["u"]
letters = [''] + list("abcdefgh")

numbersounds = {k: sound(k) for k in (n+l for n in numbers for l in letters)}

channel = None

def queue(snd):
	global channel
	while channel is not None and channel.get_busy():
		pass
	channel = snd.play()

def play(command, data):
	number = data.partition(command)[2].strip().lower()
	queue(numbersounds[number])

if __name__ == "__main__":
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
				play("Bump", data)
				queue(bump)
			elif data.startswith("Move"):
				play("Move", data)
			elif data.startswith("END"):
				break
		except KeyboardInterrupt:
			break
		except:
			pass

