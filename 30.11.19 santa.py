h = ['1', '2', '3', '4', '5', '6', '7', '8']

def deliver1():
	for house in h:
		print('is delivered in house', house)

deliver1()
print()

def deliver2(houses):
	if len(houses) == 1:
		house = houses[0]
		print('is delivered in house', house)
	else:
		 mid = int(len(houses) / 2)
		 half_1 = houses[:mid]
		 half_2 = houses[mid:]
		 print(houses, half_1, half_2)
		 deliver2(half_1)
		 deliver2(half_2)

deliver2(h)
