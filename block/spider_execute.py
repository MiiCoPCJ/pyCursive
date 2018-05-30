import time
import sched

# 导入运行的模块
import block.market.market_api

schedule = sched.scheduler(time.time, time.sleep)

def perform_command(fun, inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (fun, inc))
    print("----- Start spider symbol API %s -----" % time.time())
    fun()


def timming_exe(fun, inc=60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (fun, inc))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

if __name__ == '__main__':
    try:
        timming_exe(block.market.market_api.get_market, inc=1)
    except KeyboardInterrupt as e:
        pass