# memorybot
Helps you remember people. Maybe more applications later.

For now probably tell you stats of person with biggest face if 50% bigger than next face (1 on 1). Else do which one is closest to center. In later version if glasses are incorporated could put a box next to each face.

Very preliminary basic layout:

at any time:
	if pressed during say() end speaking and dont do anything else



on press:
	if (face_magic(picture)): #maybe make this so if you don't get a hit the first time it tries again with next 4 frames
		say("Obama (either clip of you saying it or text to speech), imported from library/ncleg/etc / last seen x, [provided by you] / North Carolina State Sen for D32.")
	else:
		say('unknown')
		on press:
			say('whomst?')
			name = record(3)
			if presspress during 3 secs:
				save picture in unknowns
				return #will be done in app later
			if press during 3 secs: #could be in record() function
				name = that

			say(name, 'good?')

			on press:
				file in knowns
				return
			on presspress:
				save picture in unknowns
				return #will be done in app later