import time

currentTime = time.time() # Get current time
print(currentTime)

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)
print(totalSeconds)
# Get the current second 
currentSecond = totalSeconds % 60 
print(currentSecond)
# Obtain the total minutes
totalMinutes = totalSeconds // 60 

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is", currentHour, ":", 
    currentMinute, ":", currentSecond, "GMT")