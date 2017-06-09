from threading import Thread
import time

def timer(name, delay, repeat):
	print(name+" started")
	while repeat>0:
		time.sleep(delay)
		print(name+":"+str(time.ctime(time.time())))
		repeat-=1
	print(name+ " done")

def main():
	t1 = Thread(target = timer, args = ("1", 1, 5))
	t2 = Thread(target = timer, args = ("2", 2, 5))
	t1.start()
	t2.start()
	
	print("Done")
	
main()	