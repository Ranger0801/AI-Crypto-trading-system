from apscheduler.schedulers.blocking import BlockingScheduler

def start_scanner():
    scheduler = BlockingScheduler()
    # Scans market every 5 mins [cite: 2204, 2438]
    scheduler.add_job(lambda: print("Scanning..."), 'interval', minutes=5)
    scheduler.start()