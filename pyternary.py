import time
hour = int(time.strftime("%H"))
print("Good Morning") if hour<12  else (print("Good Afternoon") if hour<16  else print("Good Evening"))