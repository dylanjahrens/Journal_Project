import threading
import time
import emailer

import schedule

'''
utilizes schedule module's run in background feature to continuously run program
VSCode cannot utilize schedule, run in terminal
https://schedule.readthedocs.io/en/stable/background-execution.html
'''


def run_continuously(interval=1):

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


schedule.every().day.at('21:13').do(emailer.Email().send_email)
#schedule.every().minute.at(":18").do(emailer.Email().send_email)

# Start the background thread
stop_run_continuously = run_continuously()

# Do some other things...
#time.sleep(60)
time.sleep(60*60*24) #sleep for 24 hours

# Stop the background thread
stop_run_continuously.set()

# Start the background thread again
stop_run_continuously = run_continuously()