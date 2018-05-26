import time
import sched

schedule = sched.scheduler(time.time, time.sleep)

def func(string1, float1):
    print("now is ", time.time(), "| output=", string1, float1)

print( time.time() )
schedule.enter(2,0,func,("do1", time.time()))
schedule.enter(2,0,func,("do2", time.time()))
schedule.enter(3,0,func,("do3", time.time()))
schedule.enter(4,0,func,("do4", time.time()))

schedule.run()
print(time.time())