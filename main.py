"""
Hot Fingers Lite
By ItsGreenFire

License:
PERSONAL USE ONLY
*You may not profit off of this*
"""

import time
import pyautogui as pag
import keyboard
import pygame

pag.PAUSE = 0.005  # I mean you can change this, but you prob shouldn't
active = False
clock = pygame.time.Clock()  # I'm going to be real with you, I don't know why, but without this the whole thing doesn't work
speed = 0  # THIS DEFINES THE SPACE BETWEEN CLICKS
keyStart = "r"  # CHANGE TO DESIRED KEY


def autoClick():
    pag.click(pag.position())
    time.sleep(speed)


while True:
    if keyboard.is_pressed(keyStart):
        active = True
    else:
        active = False
    if active:
        autoClick()
