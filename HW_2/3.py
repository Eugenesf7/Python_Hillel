minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60
rest_minutes = minutes % 60

print(hours, "hours", rest_minutes, "minutes")
