numbers_input = int(input("Введіть кількість секунд: "))

seconds_in_a_day = 86400
seconds_in_a_hour = 3600
seconds_in_a_minute = 60
seconds_in_a_second = 1

days = numbers_input // seconds_in_a_day
extra_seconds = numbers_input % seconds_in_a_day

hours = extra_seconds // seconds_in_a_hour
extra_seconds %= seconds_in_a_hour

minutes = extra_seconds // seconds_in_a_minute
extra_seconds %= seconds_in_a_minute

seconds = extra_seconds

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

if days == 1:
    day_word = "день"
elif days in [2, 3, 4]:
    day_word = "дні"
else:
    day_word = "днів"


print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")
