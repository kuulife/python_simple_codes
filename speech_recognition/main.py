import speech_recognition as sr
import webbrowser
import pyaudio

sr.Microphone(device_index=1)
r = sr.Recognizer()

r.energy_threshold = 5000

with sr.Microphone() as source:
	print('Ask Something ...')
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print('You asked for : '.format({text}))
		url = 'https://www.google.co.in/search?q='
		search_url = url + text
		webbrowser.open(search_url)
	except:
		print('Sorry! Can\'t recognize')