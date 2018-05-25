import time, sched

schedule = sched.scheduler(time.time, time.sleep)


def perfor_command(fun, inc):
    schedule.enter(inc, 0, perfor_command, (fun, inc))
    fun()


def timming_exe(fun, inc=60):
    schedule.enter(inc, 0, perfor_command, (fun, inc))
    schedule.run()
