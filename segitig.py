a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

L = []

a = round(a)
b = round(b)
c = round(c)

L.append(int(a))
L.append(int(b))
L.append(int(c))

L.sort()

maximum = max(L)

if ((a <= 0) or (b<=0) or (c<=0) or (a+b<=c) or (a+c<=b) or (b+c<=a) ) :
	print("segitiga tidak dapat dibangun")
elif ((a == b ==c)) :
	print("segitiga sama sisi")
elif ((a==c) or (a==b) or (b==c)) :
	print("segitiga sama kaki")
elif (maximum**2 == (L[0]**2)+(L[1]**2) ) :
	print("segitiga siku-siku")
else :
	print("segitiga bebas")