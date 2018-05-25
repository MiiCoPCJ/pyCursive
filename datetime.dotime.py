import datetime
import time

'''
time good 
'''

def doSth():
    print(u'The schemdule time')

def main(h=1,m=0):
    while True:
        now = datetime.datetime.now()
        print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
            break
        time.sleep(5)
    doSth()

if __name__ == "__main__":
    print('doing')
    main()

