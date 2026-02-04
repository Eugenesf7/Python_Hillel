seconds = int(input("Enter the number of seconds: "))

sec_in_min = 60
sec_in_hour = 60 * 60
sec_in_day = 24 * sec_in_hour

days, seconds = divmod(seconds, sec_in_day)

hours, seconds = divmod(seconds, sec_in_hour)

minutes, seconds = divmod(seconds, sec_in_min)

if days % 10 == 1 and days % 100 != 11:
    day_word = "day"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "days"
else:
    day_word = "days"

time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
result = f"{days} {day_word}, {time_str}"

print(result)
