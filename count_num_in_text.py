import re
file = open('regex_sum.txt')
numlist = list()
total_num = 0

for line in file:
    line = line.rstrip()
    num = re.findall('([0-9]+)', line)

    if len(num) < 1:
        continue
        
    for item in num:
        nums = float(item)
        total_num += nums

print(total_num)
