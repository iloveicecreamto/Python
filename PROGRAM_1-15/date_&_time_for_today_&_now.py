#Pgm to print date, time for today and now.


from datetime import datetime, time

now = datetime.now()

print("Today's Date:", now.date())
print("Current Time:", now.strftime("%H:%M:%S"))