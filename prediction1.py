
from random import random

counter = 1
data = [0]
data2 = [0]
position = 0


def dat_store(pos):
	random_num = random()
	random_num2 = random()
	data.append(random_num)
	difference = random_num2 - random_num
	data2.append(difference)

	print ("random_num1: " + str(random_num))

	print("random_num2: " + str(random_num2))
	
	print("diff:" + str(data2[pos-1]))

if (position != 0):
	position = position + 1
	
while (counter <= 100):
	print("No." + str(counter))
	dat_store(position)
	counter = counter + 1

length_data = len(data)

half_way = length_data / 2 

predict_test = int(half_way)

predict_val = data[predict_test]
predict_val2 = data2[predict_test] 

print (str(predict_val) + ": Predict Val #1")
print (str(predict_val2) + ": Predict Val #2")


