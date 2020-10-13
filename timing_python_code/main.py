#import time
import time
import timeit
def func_one(n):
	return [str(i) for i in range(n)]

#current time before 
start_time = time.time()

#run code
result = func_one(100)

#current time after
end_time = time.time()

#elapced time
elapsed_time = end_time - start_time

print(elapsed_time)

