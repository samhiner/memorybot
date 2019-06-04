import cv2

#return unknown, no face, or [name]
#TODO make sure name can't be unknown or no face. Actually maybe use numeric ID system for people
def identify(filename):
	pass

#void
def say(text):
	pass

def scan_person():
	video = cv2.VideoCapture(0)

	for x in range(5):
		_, frame = video.read()
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
		_ = cv2.imwrite('capture.jpg', frame) #TODO can i do this without making a file?
		person = identify('capture.jpg')
		if person != 'unknown' and person != 'no face': #maybe save unknown images where there was a face so if last one doesn't find a face we can still do it. 
			break										#maybe don't check 5 times as it's like p-hacking. Will have to see how accuracy is affected when done.

	video.release()
	cv2.destroyAllWindows()

	if person == 'no face':
		say('No face found.')
	elif person == 'unknown':
		say('Unkown')
		clicks = input('Clicks: ') #this would happen right after conversation
		if clicks == 'x':
			say('Who is it?')
			recording()
		else: #if you double click
			return
	else:
		say(person, get_info(person))

#while True:
#	clicks = input('Clicks: ') #this is temporary for working on desktop
scan_person()