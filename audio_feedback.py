#!/usr/bin/env python

import pygame.mixer
import socket

pygame.mixer.init()

noise = pygame.mixer.Sound(u"Buzz.wav")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 29999))

while True:
    data = sock.recv(1024)
    print data
    if data.startswith("STOP"):
        noise.stop()
    elif data.startswith("START"):
        print "foo"
        noise.play(loops=-1)
    elif data.startswith("END"):
        break

