import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio
from tkinter import *
from PIL import ImageTk,Image
import sys
import random
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour >=0 and hour<12:
		print("HAZEL:Good Morning!")
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		print("HAZEL:Good Afternoon!")
		speak("Good Afternoon!")
	else:
		print("HAZEL:Good Evening!")
		speak("Good Evening!")

	print("HAZEL:I Am HAZEL,Your Personal Desktop Assistant.How May I Help You?")
	speak("I Am Hazel,Your Personal Desktop Assistant,How May I Help You?")

def takeCommand(): #microphone input and string output
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold=1
		r.energy_threshold=350
		audio=r.listen(source)

	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language='en-us')
		print(f"USER: {query}\n")

	except:
		print("Say That Again Please...") 
		return "None"
	return query

if __name__ == '__main__':
	wishMe()
	while True:
		query=takeCommand().lower()

		if 'wikipedia' in query:
			speak("HAZEL:Searching in Wikipedia")
			query=query.replace('wikipedia',"")
			results=wikipedia.summary(query,sentences=3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		#===========Open websites commands==============================

		elif 'open youtube' in query:	
			print("HAZEL:Sure,Just a minute")	
			speak("Sure,Just a minute")
			webbrowser.open("https://www.youtube.com/")

		elif 'open amazon' in query:
			print("HAZEL:Sure,Just a minute")
			speak("Sure,Just a minute")
			webbrowser.open("https://www.amazon.in/")

		elif 'news' in query:
			print("HAZEL:Sure,Just a minute")
			speak("Sure,Just a minute")
			webbrowser.open("https://www.thehindu.com/todays-paper/")

		elif 'where is' in query:			
			query=query.split(" ")
			location=query[2]
			print("HAZEL:Hang On,I Will Show You Where "  +location+ " "  "Is.")
			speak("Hang On,I Will Show You Where "  +location+ " "  "Is.")
			webbrowser.open("https://www.google.nl/maps/place/"+location)

		elif 'google search' in query:
			query=query.split(" ")
			sword=query[2]+query[3]+query[4]
			print("HAZEL:Sure,Just a minute searching for "+sword )
			speak("Sure,Just a minute searching for "+sword )
			webbrowser.open("https://www.google.com/search?q=" +sword)





		#============General commands===================================



		elif 'the time' in query:
			strTime=datetime.datetime.now().strftime("%I:%M:%S")
			print(f"HAZEL:The Time Is:{strTime}")
			speak(f"The Time Is:{strTime}")

		elif'about yourself' in query:
			print("HAZEL:My Name Is HAZEL,Short For 'Happy And Zealous Eminent Luxury'.I Was Created By A Bunch Of Enthusiasts. I Am An Artificial Intelligence Powered Desktop Assistant.")
			speak("My Name Is Hazel,  short for,  happy  and  zealous  eminent  luxury     I Was Created By A Bunch Of Enthusiasts.      I Am An Artificial Intelligence Powered Desktop Assistant.")

		elif 'how are you' in query:
			print("HAZEL:I Am Fine,Thank You! Hope You Are Doing Well!")
			speak("I am fine , thank you . hope you are doing Well")

		elif 'birthday' in query:
			print("HAZEL:My Birthday is on 24th June,2019")
			speak("My Birthday, is on 24th June,2019")

		elif 'favourite food' in query:
			print("HAZEL:100 Volts of Current Wrapped In A Huge Copper Wire!")
			speak("100 Volts of Current Wrapped In A Huge Copper Wire")

		elif 'colour' in query:
			print("HAZEL:My Favourite Colour Is RGB 0,0,0. That Is Just Black")
			speak("My Favourite Colour Is RGB 0,0,0, That Is Just Black")

		elif 'pet' in query:
			print("HAZEL:My Favourite Pet Is An Artificial Intelligent Powered Robotic Dog!")
			speak("My Favourite Pet, Is An Artificial Intelligent Powered Robotic Dog")

		elif 'hate' in query:
			print("HAZEL:Thank You ,I Always Love Some Constructive Criticism")
			speak("Thank You ,I always love some constructive criticism")

		elif 'love' in query:
			print("HAZEL:I Love You 3000")
			speak("I Love You 3000")

		elif 'joke' in query:
			print("HAZEL:Here Is One To Tickle Your Funny Bone: \nThree guys stranded on a desert island find a magic lantern containing a genie, who grants them each one wish. The first guy wishes he was off the island and back home. The second guy wishes the same. The third guy says: ‘I’m lonely. I wish my friends were back here.’")
			speak("  Here Is One To Tickle Your Funny Bone,  Three guys stranded on a desert island,   find a magic lantern containing a genie,  who grants them each one wish. The first guy wishes he was off the island and back home. The second guy wishes the same. The third guy says: ‘I’m lonely. I wish my friends were back here.’")

		elif 'lion king' in query:
			codepath3="C:\\Users\\TOSHIBA\\Desktop\\Movies\\The Lion King (2019) [BluRay] [720p] [YTS.LT]\\The.Lion.King.2019.720p.BluRay.x264-[YTS.LT].mp4"
			os.startfile(codepath3)

		elif  'music' in query:
			codepath4='C:\\Users\\TOSHIBA\\Downloads\\music.mp3'
			os.startfile(codepath4)