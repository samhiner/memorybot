import face_recognition as fr
import math
import cv2

def get_face_by_size(face_locations):
	#these -1's are just placeholders that will never make it to the end
	largest = [-1, -1]
	next_largest = [-1, -1]
	for x in range(len(face_locations)):
		coords = face_locations[x]

		face_size = math.sqrt((coords[0] - coords[2])**2 + (coords[1] + coords[3]))
		if face_size > largest[0]:
			largest = [face_size, x]
		elif face_size > next_largest[0]:
			next_largest = [face_size, x]

	if largest[0] >= next_largest[0] * 1.5:
		return largest[1]
	else:
		return None

def face_by_center_proximity(face_locations, img_size):
	#-1 is a placeholder; not talking about end of list
	closest_to_center = [math.inf, -1]
	for x in range(len(face_locations)):
		coords = face_locations[x]

		vert_diff = abs(((coords[0] + coords[2]) / 2) - (img_size[0] / 2))
		horiz_diff = abs(((coords[1] + coords[3]) / 2) - (img_size[1] / 2))

		if vert_diff + horiz_diff < closest_to_center[0]:
			closest_to_center = [vert_diff + horiz_diff, x]

	return closest_to_center[1]

known_face = fr.face_encodings(fr.load_image_file('assets/speaking_obama.jpg'))[0] #TODO make sure that we are getting subjects face from knowns

unknown_picture = fr.load_image_file('assets/crowd_obama.jpg')
face_locations = fr.face_locations(unknown_picture)

#TODO should I put this bit in a function? 
index = None
if len(face_locations) > 1:
	index = get_face_by_size(face_locations)
	if index == None:
		index = face_by_center_proximity(face_locations, cv2.imread('assets/crowd_obama.jpg').shape[:2])

elif len(face_locations) == 1:
	index = 0
else:
	pass
	#return 'No faces'

print(face_locations[index])
unknown_face = fr.face_encodings(unknown_picture)[index]

print(fr.compare_faces([known_face], unknown_face)[0])