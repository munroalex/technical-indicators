import random, csv

completed_indicators = []
indicator_list = []
num = 1
for i in range(1, 68):
    indicator_list.append(num)
    num += 1

indicator = random.randint(1, 68)
print(indicator)
print(indicator_list)
