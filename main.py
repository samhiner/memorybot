import cv2
import datetime
import identify
import numpy as np
import os

#TODO make this speak instead of print
def say(text):
	print(text)

#TODO make this format it nicely and say files
#for that maybe just change this function to
#speak_info() and make it void
def get_info(person_id):
	with open('assets/directory.txt') as file:
		return file.readlines()[person_id]

def listen(max_time):
	return input('Listening... ')

def scan_person():
	video = cv2.VideoCapture(0)

	for x in range(5):
		_, frame = video.read()
		cv2.imwrite('capture.jpg', frame)
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) #TODO is this necessary? I forgot what it does.
		person, encoding = identify.identify(frame)
		#if it is a list it is "unknown" or "no faces"
		if person != 'no faces':						#maybe save unknown images where there was a face so if last one doesn't find a face we can still do it. 
			break										#maybe don't check 5 times as it's like p-hacking. Will have to see how accuracy is affected when done.
		else:
			print('No face found; error code: ' + person)

	video.release()
	cv2.destroyAllWindows()

	if person == 'no faces':
		say('No face found.')
	elif person == 'unknown':
		say('Unknown')
		clicks = input('Clicks: ') #this would happen right after conversation
		if clicks == 'x':
			#create directory entry
			say('Who is it?')
			name = listen(3)
			with open('assets/directory.txt') as file:
				filename = str(len(file.readlines()))
			with open('assets/directory.txt', 'a') as file:
				file.write(filename + ',' + name + ',"random data yay"\n') #TODO this needs to be cleaned up to look something like the style in the readme
			#save encoding to knowns file
			np.save((os.path.join('assets', 'knowns', filename) + '.npy'), encoding) #TODO learn more about os.path.join. Do I want my standard to be "/" or that?
		else: #if you double click
			unix_time = str(int(datetime.datetime.utcnow().timestamp())) #utc timezone to avoid overwriting pictures when switching timezones
			np.save((os.path.join('assets', 'unknowns', unix_time) + '.npy'), encoding) #TODO change this to store face encodings if they are saved for later to speed it up when this is classified
			return
	else:
		say(get_info(int(person)))

#while True:
#	clicks = input('Clicks: ') #this is temporary for working on desktop
scan_person()