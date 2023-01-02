from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import some_task
def start_jobs():

    print("starting scheduled cron jobs")
    
    scheduler = BackgroundScheduler()
    
    #Set cron to runs every 1 min.
    cron_job = {'month': '*', 'day': '*', 'hour': '*', 'minute':'*/1'}
    
    #Add our task to scheduler.
    scheduler.add_job(some_task, 'cron', **cron_job)
    

#And finally start.    
    scheduler.start()