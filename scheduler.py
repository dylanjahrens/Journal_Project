import threading
import time
import schedule


'''
Schedules a test email but does not run continuously. See background.py for 
continuously running program
'''

class EmailScheduler(threading.Thread):
    
    def __init__(self):
        super().__init__()
        self.__stop_running = threading.Event()

    #schedule daily email
    def schedule_daily(self, hour, minute, job):
        schedule.clear() #clears existing scheduled tasks
        schedule.every().day.at(f'{hour:02d}:{minute:02d}').do(job)

    #start scheduler as a background thread
    def run(self):
        self.__stop_running.clear()
        while not self.__stop_running.is_set():
            schedule.run_pending()
            time.sleep(1)

    #stop the schuduler thread
    def stop(self):
        self.__stop_running.set()

if __name__ == '__main__':
    import emailer
    email = emailer.Email()

    scheduler = EmailScheduler()
    scheduler.start()

    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min + 1 # schedule for next minute
    print(f'Scheduling test email for {hour:02d}:{minute:02d}')
    scheduler.schedule_daily(hour, minute, email.send_email)

    time.sleep(60) # keep program alive long enough to ensure send
    scheduler.stop()
