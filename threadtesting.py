import threading
import time
import cv2

while True:
	print('asshole')
	if cv2.waitKey(1) & 0xFF == ord('q'):
		print('asddas')
		break


#random expensive function
def prime_factorize(letter):
	x = ord(letter) - 96

	factors = []
	divisor = 2
	while True:
		if x == 1:
			break

		while x % divisor == 0:
			x /= divisor
			factors.append(divisor)

		divisor += 1

	return len(factors) == 3 and (factors[0] in factors[1:] or factors[2] in factors[:2])


def wee():
	for x in 'dshfjkhjkfdshscituocxkasjdhhjkdsfaiuhwefbjhckxbhyuwiefuewyuiodssdabnmewqew':
		for y in 'dshfjkhjkfdshscituocxkasjdhhjkdsfaiuhwefbjhckxbhyuwiefuewyuiodssdabnmewqew':
			for z in 'dshfjkhjkfdshscituocxkasjdhhjkdsfaiuhwefbjhckxbhyuwiefuewyuiodssdabnmewqew':
				prime_factorize(x)
				prime_factorize(y)
				prime_factorize(z)
		print('running')


def timelimit(secs):
	time.sleep(secs)

thread1 = threading.Thread(target=timelimit, args=(1,))
thread2 = threading.Thread(target=wee)

thread1.start()
thread2.start()

from timeit import default_timer as timer
startTime = timer()


while True:
	print(thread1.is_alive())
	print(thread2.is_alive())

	if not thread1.is_alive():
		#no such thing as thread2.stop(). Prob have to use Queue to get data out early/to end thread
		break
	elif not thread2.is_alive():
		#no such thing as thread1.stop(). Prob have to use Queue to get data out early/to end thread
		break


print(timer() - startTime)