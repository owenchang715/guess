import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了！')
		print('你已經猜了', count, '次')
		break
	elif num > r:
		print('比答案大，猜小一點')
	elif num < r:
		print('比答案小，猜大一點')
	print('你已經猜了', count, '次')