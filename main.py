from random import uniform, random
import  math
import sys

npoint = float(sys.argv[1])
circle_count = 0

def puntos():
	count = 0
	j = 1
	while j <= npoint:
		xcoordinate = random()
		ycoordinate = random()
		x = xcoordinate**2
		y = ycoordinate**2
		z = math.sqrt(x + y)
		if z < 1:
			count += 1
		j+=1
	return count

circle_count = puntos()
pi = 4.0 * circle_count / npoint

print(pi)
