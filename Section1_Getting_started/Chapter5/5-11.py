#! python3

numbers = [number for number in range(1,10)]

for num in numbers:
    if num >= 4:
        print("%sth" %(num))
    else:
        if num == 3:
            print("%srd" %(num))
        if num == 2:
            print("%snd" %(num))
        if num == 1:
            print("%sst" %(num))





