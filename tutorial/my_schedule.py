import schedule
import time

# Define a job function
def job():
    print("Job is running")

# Schedule the job to run every 10 seconds
schedule.every(10).seconds.do(job)

try:
    # Keep the script running to allow the job to execute
    while True:
        schedule.run_pending()
        time.sleep(1)  # Optional: Adds a 1-second delay between checks
except KeyboardInterrupt:
    print("Script interrupted. Exiting...")
