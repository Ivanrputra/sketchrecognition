from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=1, retry_after_failure_mins=1)
    code = 'sketch_recognition.my_cron_job'    # a unique code
    # code = 'sketch_recognition.MyCronJob'    # a unique code
    
    def do(self):
        print('haha')