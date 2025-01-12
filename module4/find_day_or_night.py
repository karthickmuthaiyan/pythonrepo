import time

# Get the current local time
current_time = time.localtime()

#print lcoaltime in dd/mmyy hh:mm:ss format
print(time.strftime("%d/%m/%y %H:%M:%S"))
# Extract the hour from the current time
current_hour = current_time.tm_hour

# Determine if it is day or night
if 6 <= current_hour < 18:
    print("It is day time.")
else:
    print("It is night time.")