import sys
import random
import pygame
import pygame, sys
import librosa
from pygame.locals import *
from pygame import mixer

import os,time,sys
from sys import exit
import pygame
from pygame.locals import *
from mutagen.mp3 import MP3
from random import choice
#from tkinter import *
#from tkinter.filedialog import askopenfilename
# Configuration
pygame.init()
pygame.mixer.init()
fps = 30
fpsClock = pygame.time.Clock()
width, height = 200, 350
screen = pygame.display.set_mode((width, height))
#mus=pygame.mixer.Sound("Gold_Lip_Friends_Lovers_vmusice.ogg")
#mus.play()
font = pygame.font.SysFont('Arial', 40)

windowSurfaceObj = screen
#objects = []


class Button():
	def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.onclickFunction = onclickFunction
		self.onePress = onePress

		self.fillColors = {
			'normal': '#ffffff',
			'hover': '#666666',
			'pressed': '#333333',
		}

		self.buttonSurface = pygame.Surface((self.width, self.height))
		self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

		self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

		self.alreadyPressed = False

		#objects.append(self)

	def process(self):

		mousePos = pygame.mouse.get_pos()
		
		self.buttonSurface.fill(self.fillColors['normal'])
		if self.buttonRect.collidepoint(mousePos):
			self.buttonSurface.fill(self.fillColors['hover'])

			if pygame.mouse.get_pressed(num_buttons=3)[0]:
				self.buttonSurface.fill(self.fillColors['pressed'])

				if self.onePress:
					print("88888888888888888888888888888")
					self.onclickFunction()

				elif not self.alreadyPressed:
					self.onclickFunction()
					
					self.alreadyPressed = True

			else:
				self.alreadyPressed = False

		self.buttonSurface.blit(self.buttonSurf, [
		self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
		self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
		])
		screen.blit(self.buttonSurface, self.buttonRect)

redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)

#starting position
x = 25
pygame.draw.rect(windowSurfaceObj,redColor,Rect(x,200,30,30))#polz
pygame.display.update(pygame.Rect(0,0,width,height))

s = 0

msg='TEXT'
conf_text=pygame.font.Font(None, 24)
text=conf_text.render(msg, True,(180,0,0))
p=0
paus=False
def pause():
	global p, paus
	p+=1
	if p%2==0:
		pygame.mixer.music.unpause()
		paus=False
	else:
		pygame.mixer.music.pause()
		paus=True
		#p=0
	print(p)
#def left():
#	print('left')
#def right():
#	print('right')
def sbor_mus(fidir):
		musics =[]
		ff=0
		for root, dirs, files in os.walk(fidir):
			for file in files:
				tmp =[]
				if file.endswith('mp3'):
					file = os.path.join(root,file)
					song = MP3(file)
					ff+=1
					#print(song)
					duration = round(song.info.length)
					tmp.append(file)
					tmp.append(duration)
					musics.append(tmp)
		#print(len(musics))
		global l
		l=len(musics)
		return musics
global musics
musics = sbor_mus('C:\\Users\\Станислав\\Desktop\\mp3')

def myFunction():
	
	#print(mus.get_length())
	#Tk().withdraw()
	#filename = askopenfilename()
	#t=conf_text.render(filename,True,(180,0,0))
	#creen.blit(conf_text.render('---------------------', True,(180,0,0)),(30,240))
	#sg='----------------------------------------------------------'
	#f=False
	#print(f)
	print('Button Pressed')
#global n,m
n=0
#В СЛУЧАЙНОМ ПОРЯДКЕ 
def launch():
	global n,paus,sec
	if n>=l:
		n=0
	music = musics[n]
	sec=music[1]
	#print(type(musics))
	n+=1
	pygame.mixer.music.load(music[0])
	paus=True
	pygame.mixer.music.play()
	print("Начать воспроизведение:% s -% s секунд"%(music[0] , str(sec)))
	
	return music
'''
def sing_a_song():
	# Произвольно выбрать музыкальное произведение
	music = choice(musics)
	#print(type(musics))
	pygame.mixer.music.load(music[0])
	pygame.mixer.music.play()
	#print("Начать воспроизведение:% s -% s секунд"%(music[0] , str(music[1])))
	return music
'''

def right():
	global n,p
	p=0
	n+=1
	if n>=l:
		n=0
	#elif n==0:
	
	
	music = musics[n]
	#print(type(musics))
	
	pygame.mixer.music.load(music[0])
	pygame.mixer.music.play()
	print("Начать воспроизведение:% s -% s секунд"%(music[0] , str(music[1])))
	return music

def left():
	global n,p
	p=0
	if n>0:
		n-=1
#	elif n==0:
#		continue
	music = musics[n]
	#print(type(musics))
	pygame.mixer.music.load(music[0])
	pygame.mixer.music.play()
	print("Начать воспроизведение:% s -% s секунд"%(music[0] , str(music[1])))
	return music

for i in musics:
	print(i)
sec=1
#customButton = Button(30, 30, 100, 100, 'Button One (onePress)', myFunction)
#customButton = Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)
w=h=30
btn1=Button(25, 240, w, h, 'z', launch)
btn2=Button(55, 240, w, h, 'l', left)
btn3=Button(85, 240, w, h, 'p', pause)
btn4=Button(115, 240, w, h, 'r', right)
btn5=Button(145, 240, w, h, 'z', launch)
f=True
button = pygame.mouse.get_pressed()
# Game loop.
a=25
while True:
	#print(120/242)#где 120длинна колонки а 242секунды песня
	#sing_a_song()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		pressed_keys = pygame.key.get_pressed()



	#print(n)
	button = pygame.mouse.get_pressed()
	pos = pygame.mouse.get_pos()
	x = pos[0]
	y = pos[1]
	if button[0] != 0 and 175>x>25 and 230>y>200:
		pos = pygame.mouse.get_pos()
		x = pos[0]
		y = pos[1]
		a = x - 15#где схватит, здесь по центру высчитано на -5пикс
		print(x,y)
		if a < 25:
			a = 25
		elif a>145:
			a=145

		pygame.draw.rect(windowSurfaceObj,blackColor,Rect(0,0,width,height))#okno
		#pygame.display.update(pygame.Rect(0,0,width,height))
		pygame.draw.rect(windowSurfaceObj,redColor,Rect(a,200,30,30))#polz
		pygame.display.update(pygame.Rect(0,0,width,height))

	if button[1] == 0:
		print("rrrrrrrrrrrrrrrrrrrrr")


	elif paus==True:
		pix=120/sec
		#print("120 / "+str(sec)+" = "+str(round(pix,2)))
		time.sleep(pix)
		a=a+pix
		print(a)
		pygame.draw.rect(windowSurfaceObj,blackColor,Rect(0,0,width,height))#okno
		pygame.draw.rect(windowSurfaceObj,redColor,Rect(a,200,30,30))#polz
		pygame.display.update(pygame.Rect(0,0,width,height))
		if a>=145:
			a=25


	#print(time.time())
	btn1.process()
	btn2.process()
	btn3.process()
	btn4.process()
	btn5.process()
	#print(sing_a_song())
	
	
	
	pygame.display.flip()
	fpsClock.tick(fps)
