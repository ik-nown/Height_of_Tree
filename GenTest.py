import random
import time

prev_num = 0
def inc():
    prev_num = random.randint(0, 10)
    for i in range(1000000):
        new_num = prev_num + random.randint(1, 10)
        f.write(str(round(new_num, 3)))
        f.write(" ")
        prev_num = new_num
def dec():
    prev_num = random.randint(9999991, 10000000)    
    for i in range(1000000):
        new_num = prev_num - random.randint(1, 10)
        f.write(str(round(new_num, 3)))
        f.write(" ")
        prev_num = new_num
        
        
for i in range (10):
    f = open(r"D:\HK2\DSA\Height_of_Tree\dataset\data" + str(i+1) + ".txt", "w")
    #f.truncate(0)
    random.seed(time.time())
    if (i == 0):
        inc()
    if (i == 1):
        dec()
    else:
        for i in range(1000000):
            num = random.randint(0, 1000000) 
            f.write(str(round(num, 3)))
            f.write(" ")
               



