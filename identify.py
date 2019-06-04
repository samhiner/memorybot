import face_recognition as fr
import math
import numpy as np
import os

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
	closest_to_center = [math.inf, None]
	for x in range(len(face_locations)):
		coords = face_locations[x]

		vert_diff = abs(((coords[0] + coords[2]) / 2) - (img_size[0] / 2))
		horiz_diff = abs(((coords[1] + coords[3]) / 2) - (img_size[1] / 2))

		if vert_diff + horiz_diff < closest_to_center[0]:
			closest_to_center = [vert_diff + horiz_diff, x]

	return closest_to_center[1]

def focused_face_index(unknown_picture):
	face_locations = fr.face_locations(unknown_picture)
	index = None
	if len(face_locations) > 1:
		index = get_face_by_size(face_locations)
		if index == None:
			return face_by_center_proximity(face_locations, unknown_picture.shape[:2])
	elif len(face_locations) == 1:
		return 0
	else:
		return 'no faces'

def identify(unknown_picture):
	#get unknown face encoding
	index = focused_face_index(unknown_picture)
	if index == 'no faces':
		return 'no faces', None
	unknown_face = fr.face_encodings(unknown_picture)[index]

	with open('assets/directory.txt') as file:
		for line in file:
			curr_id = line.split(',')[0]
			known_face = np.load((os.path.join('assets', 'knowns', curr_id) + '.npy'))
			if fr.compare_faces([known_face], unknown_face)[0]:
				return curr_id, None

		return 'unknown', unknown_face