x = int(input("1: "))
y = int(input("2: "))

i = 1

r = [];

while True:
	if x % i == 0:
		if x == i:
			r.append(i)
			break
		else:
			r.append(i)
			i+=1
	else:
		i+=1
		continue

s = len(r)-1


for j in range(1,len(r)+1):

	d = r[s]
	if d == 1:
		print "nothing..."
		break

	s-=1

	if y % d == 0:
		print str(d)
		break
	else:
		continue