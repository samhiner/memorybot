import threading
import time

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


def timelimit(secs):
	time.sleep(secs)

thread1 = threading.Thread(target=timelimit, args=(1,))
thread2 = threading.Thread(target=wee)

thread1.start()
thread2.start()

from timeit import default_timer as timer
#TODO redo this with imported file so that the time that it takes to set up the Disintegrate function is counted
#TODO make Disintegrate function-specific if you want
startTime = timer()


while True:
	print(thread1.is_alive())
	print(thread2.is_alive())

	if not thread1.is_alive():
		#should kill both?
		break
	elif not thread2.is_alive():
		#should kill both?
		break


print(timer() - startTime)