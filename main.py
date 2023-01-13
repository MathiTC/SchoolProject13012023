from datetime import datetime, timedelta

sleep_hours = int(input("How many hours do you want to sleep? "))
current_time = datetime.now()
wakeup_time = current_time + timedelta(hours=sleep_hours)

print("Current time:", current_time.strftime("%H:%M:%S"))
print("Wakeup time:", wakeup_time.strftime("%H:%M:%S"))
